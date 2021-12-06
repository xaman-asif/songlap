from django.http.response import HttpResponse
from django.shortcuts import render
from post.models import Replies
from post.models import Post

# Create your views here.
'''

def Reply(request,id):
  s1=Post.objects.get(id=id)

  if (request.method == 'GET'):
    return render(request,'reply/index.html',{'read_post':s1})
  elif (request.method == 'POST'):	
    
   p1=request.POST.get('content')
   p2=request.POST.get('custId')
   b = Replies(post=p1, reply_txt=p2)
   b.save()
   messages.info(request,"replied")
   return redirect('reply')
'''
def See(request):
	context = { 
		'posts': Replies.objects.all()
	}
	return render(request, 'reply/see_reply.html', context)

		
