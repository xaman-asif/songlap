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
  
  elif request.headers.get('x-requested-with') == 'XMLHttpRequest': 
    
    rep_ly = json.load(request)['rep_ly'] 
    r=Replies.objects.create(
     post=obj,
     reply_txt=rep_ly

     )
    r.save()
    data={
      "replied": rep_ly

    } 
    return JsonResponse(data, status=200) 
  

def DeleteReply(request):
  key = request.GET.get('id')
  del_post = Replies.objects.get(id = key)
  del_post.delete()

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def editreply(request,id,post_id):
 
  edit_rep = Replies.objects.get(id = id)
  
  context = { 
    'old_reply': edit_rep,
    'p_id':post_id
  }

  if (request.method == 'GET'):
   
    return render(request, 'reply/edit_reply.html',context)
  elif(request.method == 'POST'):
    edit_rep.reply_txt=request.POST.get('content','')
    edit_rep.save()
  
  return redirect('reply',post_id)