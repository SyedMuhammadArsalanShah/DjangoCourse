from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.index , name="Home"),
    path('about/', views.about , name="about"),
    path('ser/', views.service , name="ser"),
  
]
