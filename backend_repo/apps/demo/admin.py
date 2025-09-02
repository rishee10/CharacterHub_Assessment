from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'timestamp', 'user')
    search_fields = ('text', 'user__username')
    list_filter = ('timestamp', 'user')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'timestamp', 'post', 'user')
    search_fields = ('text', 'user__username', 'post__text')
    list_filter = ('timestamp', 'user', 'post')
