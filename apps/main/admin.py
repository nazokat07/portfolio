from django.contrib import admin
from .models import *

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('name',)

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    ordering = ('title',)


