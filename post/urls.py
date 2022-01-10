from django.urls import path
from . import views

urlpatterns = [

  
  path('upload/',views.uploadPost, name ='upload'),

  path('delete_post/',views.DeletePost,name='delete_post'),
  path('<str:category>/edit-post/<str:id>/',views.editPostView,name='edit_post'),
  path('<str:category>/edit/<str:id>/',views.editPost,name='edit'),
  path('<str:category>/<str:id>/',views.Posts,name='post'),

      
]