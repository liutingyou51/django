from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_beforelogin,name='index_beforelogin'),
    path('register',views.register,name='register'),
    path('index',views.index,name='index'),
    path('myarticle_addtime',views.myarticle_addtime,name="myarticle_addtime"),
    path('content',views.content,name="content"),
    path('post_article_choose',views.post_article_choose,name='post_article_choose'),
    path('post_article_write',views.post_article_write,name='post_article_write'),
    path('myarticle_collect',views.myarticle_collect,name="myarticle_collect"),
]
