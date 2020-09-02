from django.db import models
from django.utils import timezone


# Create your models here.
#verbose name 預設為變數名稱，可以用''改
#post db
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False)
    kind = models.CharField(max_length=100, null=True)
    pub_date = models.DateTimeField('date published')#標題從pub_date->date published ,用了verbose name
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_post = models.ForeignKey('post', on_delete = models.CASCADE)
    comment_content= models.TextField(blank=False)
    comment_datetime = models.DateTimeField(null=False, default = timezone.now)

    