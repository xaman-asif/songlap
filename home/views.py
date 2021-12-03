from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Categories


def home(request):
    categories = Categories.objects.all()
    return render(request, 'home/index.html', {'categories':categories})


def viewcategory(request, category_pk):
    try:
        todo = get_object_or_404(Categories, pk=category_pk)
        return redirect("https://www.google.com/")
    except ValueError:
        pass
