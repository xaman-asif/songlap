from django.http.response import (HttpResponse, HttpResponseRedirect)
from django.shortcuts import (redirect, render, get_object_or_404)
from django.core.files.storage import FileSystemStorage
from post.forms import UserPostForm, userPostCategory
from django.db.models import Q
from post.models import Post, PostCategory
from django.http import JsonResponse

from django.core import serializers

# Create your views here.


def Posts(request,category,id):
  form= UserPostForm()

 

  # category=request.GET.get('category')
  # id=request.GET.get('id')

  posts=list(Post.objects.filter(Q(category__name__contains=category) ).values())
  
  context= {'form':form,'posts':posts,'category':category,'id':id}
  
  return JsonResponse({'post':posts,'id':id},safe=False)



def uploadPost(request):


  if request.method == "POST":
    form = UserPostForm(request.POST, request.FILES)
    


    if form.is_valid():

      #form.save()

      instance = form.save(commit=False)
      id=request.POST.get('id')

      category=PostCategory.objects.get(id=id)
    
      instance.category= category

      instance.save()
      
      

      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))









def editPostView(request):

  id=request.GET.get('id')
  post=Post.objects.get(id=id)

  return render(request,'post/edit_post_view.html',{'post':post,'id':id})



def editPost(request):
  id=request.GET.get('id')
  title=request.POST.get('title')
  description=request.POST.get('description')


  post=Post.objects.filter(id=id).update(
    title=title,
    description=description
  )

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))












def DeletePost(request, id):

  context ={}

  obj = get_object_or_404(Post, id = id)

  if request.method == "POST":
    obj.delete()

    return HttpResponseRedirect("/")
  return render(request, "post/delete_post.html", context)

 
  




 


