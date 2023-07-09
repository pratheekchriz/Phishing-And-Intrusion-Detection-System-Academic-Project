from django.contrib import admin  
from django.urls import path  
from Authentication import views  
from django.http import HttpResponse

urlpatterns = [  
    path('dashboard/',views.home, name="home"),
    path('',views.LoginView, name="login"), 
    path('service',views.service , name="service"),
    path('contact',views.contact , name="contact"),
    ]

