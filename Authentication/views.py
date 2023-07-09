from django.shortcuts import render, redirect  
from django.contrib import messages
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request, 'dashboard-user.html')

def LoginView(request):
    return render(request, "login.html")

def logoutPage(request):
    logout(request)
    return redirect('home')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')