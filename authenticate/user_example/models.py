from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class NewUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,default=' ')
    name = models.CharField(max_length=100,default=' ')
    gender = models.CharField(max_length=100,default=' ')
    