from django.urls import path
from . import views

urlpatterns = [

  path('/<int:id>',views.Reply,name='reply'),
  path('delete_reply/',views.DeleteReply,name='delete_reply'),
  path('/editreply/<int:id>/<int:post_id>',views.editreply,name='editreply')
    
]