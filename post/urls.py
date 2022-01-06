from django.urls import path
from . import views

urlpatterns = [

  path('',views.Posts,name='post'),
  path('upload/',views.uploadPost, name ='upload'),
  path('<id>/delete_post/',views.DeletePost,name='delete_post')
      
]