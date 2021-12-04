from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/',include('post.urls')),
    path(r'', views.home),
    path('<str:category_pk>', views.viewcategory, name='category'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)