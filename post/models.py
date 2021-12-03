from django.db import models
from django.utils.translation import activate
from home.models import Categories


# Create your models here.
class Post(models.Model):
    #id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    
    viewed = models.IntegerField()
    replies = models.IntegerField()
    latest = models.DateTimeField()

    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
