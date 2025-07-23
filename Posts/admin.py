from django.contrib import admin
from .models import Posts, Like


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_datetime')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_datetime')

