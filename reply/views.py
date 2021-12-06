from django.http.response import HttpResponse,HttpResponseRedirect

from post.models import Replies
from post.models import Post
from django.shortcuts import redirect, render

# Create your views here.


def Reply(request,id):
  s1=Post.objects.get(id=id)

  if (request.method == 'GET'):
    return render(request,'reply/index.html',{'read_post':s1})
  elif (request.method == 'POST'):	


    category1=request.POST.get('content')
    category2=request.POST.get('custId')

    r=Replies.objects.create(
     post=s1,
     reply_txt=category1

     )
    r.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    
    '''
   p1=request.POST.get('content','')
   p2=request.POST.get('custId','')
   b = Replies(post=p1, reply_txt=p2)
   b.save()
   messages.info(request,"replied")
   return redirect('reply')

   '''

    #category=request.GET.get('category')

    # Post.objects.create(
    #  category=category
    # )
    
'''
def See(request):
	context = { 
		'posts': Replies.objects.all()
	}
	return render(request, 'reply/see_reply.html', context)

	'''	
