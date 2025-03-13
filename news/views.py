from django.shortcuts import render
from .models import NewsIndexPage, NewsArticlePage

# Create your views here.
def test_view(request):
    """A simple view for testing purposes"""
    news_page = NewsIndexPage.objects.first()
    articles = NewsArticlePage.objects.live().order_by('-date')
    
    return render(request, 'news/test.html', {
        'news_page': news_page,
        'articles': articles,
    }) 