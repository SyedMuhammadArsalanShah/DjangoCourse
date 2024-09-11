from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.index,name="Home"),
    path('contact/', views.contact,name="contact"),
    path('about/', views.about,name="about"),
    path('service/', views.service,name="service"),
    
]
