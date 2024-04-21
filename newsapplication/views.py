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
    response = render(request, 'single_article.html', {'article': article , 'comments': comments, 'comments_count': comments.count()})

    # Check if the 'viewed' cookie is set
    if 'article_viewed_' + str(article.id) not in request.COOKIES:
        article.views = article.views + 1
        article.save()
        # Set 'viewed' cookie to track the visit for 24 hours
        response.set_cookie('article_viewed_' + str(article.id), 'true', max_age=86400) 
        return response
    
    return response

def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category).annotate(comments_count=Count('comment'))

    return render(request, 'category_articles.html', {'category': category, 'articles': articles, 'current_category_slug': category.slug})

def search_feature(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        articles = Article.objects.filter(title__contains=search)
        return render(request, 'search_page.html', {'articles': articles, 'search_word': search})
    else:
        return render(request, 'search_page.html', {})