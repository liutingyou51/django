from django.urls import path
from . import views
app_name = 'reg'
urlpatterns = [
    path('content',views.content,name="content"),
    path('post_article_choose',views.post_article_choose,name='post_article_choose'),
    path('post_article_write',views.post_article_write,name='post_article_write'),
    path('', views.home_beforelogin, name='beforelogin'),#首頁放home_beforelogin
    path('Validate',views.registerValidate,name="register_validate"), 
]
