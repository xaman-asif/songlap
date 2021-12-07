from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from post.forms import UserPostForm, userPostCategory
from django.db.models import Q
from post.models import Post, PostCategory

# Create your views here.


def Posts(request):
  form= UserPostForm()

  category=request.GET.get('category')
  id=request.GET.get('id')

  posts=Post.objects.filter(Q(category__name__contains=category) )
  
  context= {'form':form,'posts':posts,'category':category,'id':id}
  return render(request,'post/index.html',context)



def uploadPost(request):


  if request.method == "POST":
    form = UserPostForm(request.POST, request.FILES)
   # post_category=userPostCategory(request.POST or None)


    #category=request.GET.get('category')

    # Post.objects.create(
    #  category=category
    # )
    


    if form.is_valid():

      #form.save()

      instance = form.save(commit=False)
      id=request.POST.get('id')

      category=PostCategory.objects.get(id=id)

        # for obj in instance:
        #   obj.foreign_key = 1
        #   obj.save()

      instance.category= category

      instance.save()
      
      

      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



  # if request.method=='POST':
  #   Post.objects.create(
  #     title=request.POST.get('title'),
  #     description=request.POST.get('description'),
  #     image=request.POST.get('image')
  #   )

 # return redirect('post')




