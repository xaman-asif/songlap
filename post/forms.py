from django.forms import ModelForm

from .models import Post

class UserPostForm(ModelForm):  
    class Meta:  
        model = Post
        fields = ['title','description','image']