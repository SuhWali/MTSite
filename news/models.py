from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
import re
from math import ceil
from django.utils.html import strip_tags

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock, CharBlock
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from core.blocks import BaseStreamBlock, SubscribeBlock


@register_snippet
class Author(models.Model):
    """
    Author snippet model for reuse across the site
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    bio = RichTextField(blank=True)
    email = models.EmailField(blank=True)
    twitter_handle = models.CharField(max_length=50, blank=True)
    
    panels = [
        MultiFieldPanel([
            FieldPanel('first_name'),
            FieldPanel('last_name'),
        ], heading="Name"),
        FieldPanel('photo'),
        FieldPanel('bio'),
        MultiFieldPanel([
            FieldPanel('email'),
            FieldPanel('twitter_handle'),
        ], heading="Contact Information"),
    ]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['last_name', 'first_name']


class NewsArticlePageTag(TaggedItemBase):
    """
    Bridge table for tagging NewsArticlePage objects
    """
    content_object = ParentalKey(
        'NewsArticlePage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class NewsIndexPage(Page):
    """
    The main news page that holds all news articles
    """
   
    subscribe = StreamField([
        ('subscribe', SubscribeBlock()),
    ], blank=True, null=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('subscribe'),
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        
        # Get all articles
        all_articles = NewsArticlePage.objects.live().descendant_of(self).order_by('-date')
        
        # Filter by tag if present in request
        tag = request.GET.get('tag')
        if tag:
            all_articles = all_articles.filter(tags__name=tag)
        
        # Get top 5 articles for carousel
        context['carousel_articles'] = all_articles[:5]
        
        # Paginate all articles
        paginator = Paginator(all_articles, 12)  # 12 articles per page (4 rows of 3)
        page = request.GET.get('page')
        
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
            
        context['articles'] = articles
        
        # Add the tag to the context if it exists
        if tag:
            context['current_tag'] = tag
            
        return context
    
    class Meta:
        verbose_name = "News Page"


class NewsArticlePage(Page):
    """
    A news article page
    """
    date = models.DateField("Post date", default=timezone.now)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body2 = StreamField(BaseStreamBlock(), blank=True, null=True)
    
    # Add author field
    author = models.ForeignKey(
        'news.Author',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='news_articles'
    )
    
    # Add tags field
    tags = ClusterTaggableManager(through=NewsArticlePageTag, blank=True)
    
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('tags'),
    ]
    
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('intro'),
        FieldPanel('image'),
        FieldPanel('body2'),
        FieldPanel('tags'),
    ]
    
    def get_related_articles(self):
        """
        Returns up to 4 related articles that share at least one tag with this article,
        ordered by most recent publication date
        """
        # Get the tags for this article
        tags = self.tags.all()
        if not tags:
            return []
            
        # Get articles that share at least one tag with this article
        related_articles = NewsArticlePage.objects.live().filter(
            tags__name__in=[tag.name for tag in tags]
        ).exclude(
            id=self.id  # Exclude the current article
        ).distinct().order_by('-date')
        
        # Return at most 4 related articles
        return related_articles[:4]
    
    def get_reading_time(self):
        """
        Calculate the estimated reading time in minutes.
        Average reading speed: 200-250 words per minute.
        We'll use 225 words per minute as our baseline.
        """
        # Get text from body and body2
        text = ""
        
        # Add text from RichTextField body
        if self.body:
            text += strip_tags(self.body)
        
        # Add text from StreamField body2
        if self.body2:
            for block in self.body2:
                if hasattr(block, 'value') and isinstance(block.value, str):
                    text += strip_tags(block.value)
                elif block.block_type == 'paragraph':
                    text += strip_tags(block.value)
                elif block.block_type == 'heading':
                    text += strip_tags(block.value['heading'])
                elif block.block_type == 'quote':
                    text += strip_tags(block.value['quote'])
                    if 'attribution' in block.value:
                        text += " " + strip_tags(block.value['attribution'])
        
        # Add intro text
        text += self.intro
        
        # Count words (split by whitespace and filter out empty strings)
        words = [word for word in re.split(r'\s+', text) if word]
        word_count = len(words)
        
        # Calculate reading time (225 words per minute)
        reading_time_minutes = word_count / 225
        
        # Round up to nearest minute, with a minimum of 1 minute
        return max(1, ceil(reading_time_minutes))
    
    class Meta:
        verbose_name = "News Article" 