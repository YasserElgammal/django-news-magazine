from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category
from .models.comment import Comment
from django.db.models import Count

# Create your views here.
def index(request):
    latest_articles = Article.objects.select_related('category', 'user').annotate(comments_count=Count('comment')).order_by('-created_at')
    trends_articles = Article.objects.select_related('category').order_by('-views')[:10]
    featured_articles = Article.objects.filter(is_featured=True)
    
    return render(request, 'index.html', {'latest_articles': latest_articles, 'trends_articles': trends_articles, 'featured_articles': featured_articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(article=article).select_related('user')
    
    return render(request, 'single_article.html', {'article': article , 'comments': comments})

def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category).annotate(comments_count=Count('comment'))

    return render(request, 'category_articles.html', {'category': category, 'articles': articles})