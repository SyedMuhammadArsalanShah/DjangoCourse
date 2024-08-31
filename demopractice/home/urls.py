from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="Contact"),
    path('service/', views.service, name="Service"),

 
]
