from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from post.models import PostCategory





def home(request):
    categories = PostCategory.objects.all()
    return render(request, 'home/index.html', {'categories':categories})


# def viewcategory(request, category_pk):
#     try:
#         todo = get_object_or_404( PostCategory, pk=category_pk)
#         return redirect("https://www.google.com/")
#     except ValueError:
#         pass
