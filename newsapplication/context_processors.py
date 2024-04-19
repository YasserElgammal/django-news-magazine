# context_processors.py
from .models.category import Category
from .models.setting import Setting
from django.core.cache import cache

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def settings(request):
    all_settings = Setting.objects.all()
    settings_dict = {setting.key: setting.value for setting in all_settings}
    return {'settings': settings_dict}
