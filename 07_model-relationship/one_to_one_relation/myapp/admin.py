from django.contrib import admin
from .models import Page, Like


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'page_category', 'page_publish_date', 'user']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['page_id', 'page_name', 'page_category', 'page_publish_date', 'user', 'like']