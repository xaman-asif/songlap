from django import forms
from django.db import models
from django.forms import widgets








class PostCategory(models.Model):
    name = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True)
    publish = models.DateTimeField(auto_now_add=True)
    image= models.ImageField(upload_to='images/',null=True)
    viewed = models.IntegerField(null=True)
    latest = models.DateTimeField(null=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)


    
    def __str__(self) -> str:
        return self.title
         
    
    class Meta:
      ordering=['-publish']
    #   widgets = {
    #            'class': 'firstName form-control bg-white border-left-0 border-md'
    #       }


class Replies(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    reply_txt=models.CharField(max_length=250,null=True)
    reply_time=models.DateTimeField(auto_now=True)
    replyCount=models.IntegerField(null=True)
    
