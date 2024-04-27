from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage ,name='homePage'),
    path('category/<int:id>/', views.getCategoryArticles , name='getCategoryArticles'),
    path('article/<int:id>/', views.getArticleDetails , name='getArticleDetails'),
]
