from django.forms import ModelForm
from django import forms


from .models import Post

class UserPostForm(ModelForm):  
    class Meta:  
        model = Post
        fields = ['title','description','image','category']

        # widgets = {
        #     'category': forms.HiddenInput(),
             
        # }
        