from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('register/', views.register, name='register'),
]
