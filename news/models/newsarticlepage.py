from django.db import models


from django.utils import timezone
import re
from math import ceil
from django.utils.html import strip_tags

from wagtail.models import Page


from wagtail.search import index

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField

from core.blocks import BaseStreamBlock, SubscribeBlock
from modelcluster.contrib.taggit import ClusterTaggableManager

from ..models.models import NewsArticlePageTag # Ensure the through model is imported or referenced





class NewsArticlePage(Page):
    """
    A news article page
    """
    parent_page_types = ['news.NewsIndexPage']
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
    SubscribeBlock = StreamField(
        [('subscribe', SubscribeBlock())],
        blank=True,
        null=True
    )
    
    # Add author field
    author = models.ForeignKey(
        'news.Author',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='news_articles'
    )
    
    # Add tags field
    tags = ClusterTaggableManager(through=NewsArticlePageTag, blank=True, verbose_name="Tags", help_text="A comma-separated list of tags.")
    
    
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.RelatedFields('author', [
            index.SearchField('first_name'),
            index.SearchField('last_name'),
        ]),
        index.SearchField('tags'),
    ]
    
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('intro'),
        FieldPanel('image'),
        FieldPanel('body2'),
        FieldPanel('tags'),
        FieldPanel('SubscribeBlock'),
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
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # Add any search-related context if necessary
        return context
    
    class Meta:
        verbose_name = "News Article"