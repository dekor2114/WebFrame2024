from django.urls import path, include
from . import views

urlpatterns = [
    path('about_me/', views.about_me), #127.0.0.1:8000/about_me/ 
    path('', views.landing), #127.0.0.1:8000/ 
]