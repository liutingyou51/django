from django.contrib import admin
from . models import NewUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class User_admin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'nickname','phone')
admin.site.register(NewUser, User_admin)
#如果想看superuser，User_admin 改成 UserAdmin
#superuser: user, codingx

