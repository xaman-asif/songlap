from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def Reply(request):
  return render(request,'reply/index.html')
