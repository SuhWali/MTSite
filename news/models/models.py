from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from wagtail.models import Page
from wagtail.fields import  StreamField
from wagtail.admin.panels import FieldPanel



from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase

from core.blocks import SubscribeBlock




class NewsArticlePageTag(TaggedItemBase):
    """
    Bridge table for tagging NewsArticlePage objects
    """
    content_object = ParentalKey(
        'news.NewsArticlePage',
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
        from .newsarticlepage import NewsArticlePage
        
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


