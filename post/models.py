from django.db import models
from django.utils.translation import activate
from home.models import Categories


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    publish = models.DateTimeField(auto_now_add=True)
    image= models.ImageField(upload_to='images/',null=True)
    viewed = models.IntegerField(null=True)
    latest = models.DateTimeField(null=True)
    #category = models.ForeignKey(Categories, on_delete=models.CASCADE)



    def __str__(self) -> str:
        return self.title

    
    
    
    class Meta:
     ordering=['-publish']


class Replies(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    reply_txt=models.CharField(max_length=250,null=True)
    reply_time=models.DateTimeField(auto_now=True)
    replyCount=models.IntegerField(null=True)
    
