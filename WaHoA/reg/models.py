from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class NewUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,default=' ')
    name = models.CharField(max_length=100,default=' ')
    gender = models.CharField(max_length=100,default=' ')
    birth = models.DateTimeField('birthday', null=True)