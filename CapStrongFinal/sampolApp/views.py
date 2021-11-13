from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import View
from . forms import *
from . models import *

def register(request):
   
    return render(request, 'register.html')

def index(request):
   
    return render(request, 'index.html')
    
def login(request):
   
    return render(request, 'login.html')

def dashboard(request):
   
    return render(request, 'dashboard.html')

