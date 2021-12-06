from django.forms import ModelForm
from django import forms


from .models import Post, PostCategory

class UserPostForm(ModelForm):  

    class Meta:  
        model = Post
        fields = ['title','description','image','category']

        # widgets = {
        #     'category': forms.HiddenInput(),
             
        # }
class userPostCategory(ModelForm):
    class Meta:
        model= PostCategory
        fields="__all__"

        