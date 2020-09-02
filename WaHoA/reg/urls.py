from django.urls import path
from . import views
app_name = 'reg'
urlpatterns = [
    path('content',views.content,name="content"),
    path('', views.home_beforelogin, name='beforelogin'),#首頁放home_beforelogin
    path('validate',views.registerValidate,name="register_validate"), 
]
