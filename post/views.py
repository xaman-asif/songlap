from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from post.forms import UserPostForm

from post.models import Post

# Create your views here.


def Posts(request):
  form= UserPostForm()

  


  context= {'form':form}
  return render(request,'post/index.html',context)



def uploadPost(request):


  if request.method == "POST":
    form = UserPostForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()
      return redirect('post')



  # if request.method=='POST':
  #   Post.objects.create(
  #     title=request.POST.get('title'),
  #     description=request.POST.get('description'),
  #     image=request.POST.get('image')
  #   )

 # return redirect('post')

