from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category
from django.db.models import Count

# Create your views here.
def index(request):
    latest_articles = Article.objects.select_related('category', 'user').annotate(comments_count=Count('comment')).order_by('-created_at')
    trends_articles = Article.objects.select_related('category').order_by('-views')[:10]

    return render(request, 'index.html', {'latest_articles': latest_articles, 'trends_articles': trends_articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    
    return render(request, 'single_article.html', {'article': article})

def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category)

    return render(request, 'category_articles.html', {'category': category, 'articles': articles})