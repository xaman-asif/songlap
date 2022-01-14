from django.urls import path

from . import views
urlpatterns = [
  path('<str:category>/upload/',views.uploadPost, name ='upload'),
  path('<str:category>/<str:id>/delete',views.DeletePost,name='delete_post'),
  path('<str:category>/<str:id>/edit',views.editPostView,name='edit_post'),
  path('<str:category>/<str:id>/edit/Confirm',views.editPost,name='edit'),
  path('<str:category>/',views.Posts,name='post'), 
  path('<str:category>/<str:id>/reply',views.Reply,name='reply'),
  path('<str:category>/<str:id>/delete_reply/<str:rep>',views.DeleteReply,name='delete_reply')
]
