from django.http.response import HttpResponse,HttpResponseRedirect

from post.models import Replies
from post.models import Post
from django.shortcuts import redirect, render

# Create your views here.


def Reply(request,id):
  obj =Post.objects.get(id=id)
  context = { 
    'read_post': Post.objects.get(id=id),
    'rep': Replies.objects.filter(post=id)
  }

  if (request.method == 'GET'):
    return render(request,'reply/index.html',context)
  elif (request.method == 'POST'):	


    category1=request.POST.get('content')
    category2=request.POST.get('custId')

    r=Replies.objects.create(
     post=obj,
     reply_txt=category1

     )
    r.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def DeleteReply(request):
  key = request.GET.get('id')
  del_post = Replies.objects.get(id = key)
  del_post.delete()

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

