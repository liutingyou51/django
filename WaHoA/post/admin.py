from django.contrib import admin
from .models import Post,Comment

class Post_admin(admin.ModelAdmin):
    list_display = ('title', 'content', 'kind','pub_date')
admin.site.register(Post, Post_admin)
class Comment_admin(admin.ModelAdmin):
    list_display = ('comment_content','comment_datetime')
admin.site.register(Comment,Comment_admin)