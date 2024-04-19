from django.db import models

class Setting(models.Model):
    key = models.CharField(max_length=200)
    value = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.key