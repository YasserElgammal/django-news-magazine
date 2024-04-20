from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"