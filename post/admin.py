from django.contrib import admin

from .models import Post, PostCategory,Replies

# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Replies)


