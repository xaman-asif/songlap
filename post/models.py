from django import forms
from django.db import models
from django.forms import widgets








class PostCategory(models.Model):
    name = models.CharField(max_length=20,null=True, default='',blank=True)

    def __str__(self):
        return self.name



# Create your models here.
class Post(models.Model):
    user_name=models.CharField(max_length=100,blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True)
    publish = models.DateTimeField(auto_now_add=True)
    image= models.ImageField(upload_to='images/',null=True)
    viewed = models.IntegerField(null=True)
    latest = models.DateTimeField(null=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, default='', blank=True)

    class Meta:
      ordering=['-publish']
     
   

    
    def __str__(self) -> str:
        return self.title
         
    
    
    #   widgets = {
    #            'class': 'firstName form-control bg-white border-left-0 border-md'
    #       }


class Replies(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    reply_txt=models.CharField(max_length=250,null=True)
    reply_time=models.DateTimeField(auto_now=True)
    replyCount=models.IntegerField(null=True)
    
