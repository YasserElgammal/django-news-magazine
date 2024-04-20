from django.db import models
from django.contrib.auth.models import User
from .category import Category

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    views = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/articles', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title