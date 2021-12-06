from django.urls import path
from . import views

urlpatterns = [

  #path('reply/<int:id>',views.Reply,name='reply'),
  path('see/',views.See,name='see_rep')
    
]