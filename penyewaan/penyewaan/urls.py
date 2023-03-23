from django.contrib import admin
from django.urls import path,include
from .import views
# static
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('home/', include('penyewaanApp.urls', namespace='home')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
