from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import JsonResponse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from post.forms import UserPostForm, userPostCategory
from post.models import Post, PostCategory, Replies

# Create your views here.

def Posts(request,category):
  form= UserPostForm()

 

  # category=request.GET.get('category')
  # id=request.GET.get('id')

  posts=list(Post.objects.filter(Q(category__name__contains=category) ))
  
  context= {'form':form,'posts':posts,'category':category,'id':id}


  return render(request,'post/index.html',context)

  # return JsonResponse({'post':posts,'id':id},safe=False)



def uploadPost(request, category):


  if request.method == "POST":
    form = UserPostForm(request.POST, request.FILES)
    


    if form.is_valid():

      #form.save()

      instance = form.save(commit=False)
      # id=request.POST.get('id')

      # category=PostCategory.objects.get(id=id)
    
      instance.category= category

      instance.save()
      
      print(category)

      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))









def editPostView(request,id,category):

  post=Post.objects.get(id=id)

  return render(request,'post/edit_post_view.html',{'post':post,'id':id,'category':category})
  



def editPost(request,id,category):
 
  title=request.POST.get('title')
  description=request.POST.get('description')


  Post.objects.filter(id=id).update(
    title=title,
    description=description
  )

  return redirect('/b/' + category)












def DeletePost(request, category, id):

  print(id)

  context ={}

  obj = get_object_or_404(Post, id = id)

  if request.method == "POST":
    obj.delete()

    return HttpResponseRedirect("/")
  return render(request, "post/delete_post.html", context)

 
  




 
def Reply(request, category, id):
  obj =Post.objects.get(id=id)
  context = { 
    'read_post': Post.objects.get(id=id),
    'rep': Replies.objects.filter(post=id)
  }

  if (request.method == 'GET'):
    return render(request,'post/reply.html',context)
  elif (request.method == 'POST'):	


    category1=request.POST.get('content')
    category2=request.POST.get('custId')

    r=Replies.objects.create(
     post=obj,
     reply_txt=category1

     )
    r.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def DeleteReply(request, category, id, rep):
  #key = request.GET.get('id')
  del_post = Replies.objects.get(id = rep)
  del_post.delete()

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

