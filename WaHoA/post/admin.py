from django.contrib import admin
from .models import Post

class Post_admin(admin.ModelAdmin):
    list_display = ('title', 'content', 'kind','pub_date')
admin.site.register(Post, Post_admin)