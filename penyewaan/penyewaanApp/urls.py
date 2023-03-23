from django.urls import path
from . import views

app_name= 'penyewaanApp'

urlpatterns = [
    path('sewa/', views.sewa, name='sewa'),
    path('detail/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
]