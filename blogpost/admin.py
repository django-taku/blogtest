from django.contrib import admin
from .models import SampeModel, BlogModel

# Register your models here.

# 管理画面にモデルを認証させる
admin.site.register(SampeModel)
admin.site.register(BlogModel)