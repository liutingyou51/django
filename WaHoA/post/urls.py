from django.urls import path, include 
from . import views
app_name = 'post'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('myarticles/', views.get_post, name = 'myarticles'),
    path('myfavorite/', views.get_favorite, name = 'myfavorite'),
    path('add_comment_2/',views.add_comment_2,name='add_comment_2'),
]