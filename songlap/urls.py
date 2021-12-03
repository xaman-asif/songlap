from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.home),
    path('<str:category_pk>', views.viewcategory, name='category'),
]
