from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from newsapplication.models import Article, Category
from  api.serializers import ArticleSerializer, CategorySerializer, SettingSerializer



@api_view(['GET'])
def homePage(request):
    categories = Category.objects.all()
    serializersCategories = CategorySerializer(categories, many=True)
    return Response({'categories':serializersCategories.data})

@api_view(['GET'])
def getCategoryArticles(request, id):
    category = get_object_or_404(Category, id=id)
    articles = Article.objects.filter(category=category)
    serializersArticles = ArticleSerializer(articles, many=True)
    return Response({'articles':serializersArticles.data})

@api_view(['GET'])
def getArticleDetails(request, id):
    article = get_object_or_404(Article, id=id)
    serializersArticle = ArticleSerializer(article).data
    serializersArticle['category'] = article.category.title
    serializersArticle['user'] = article.user.username
    return Response({'articles':serializersArticle})