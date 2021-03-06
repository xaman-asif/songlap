from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('post/',include('post.urls')),
    path('reply',include('reply.urls'))

  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)