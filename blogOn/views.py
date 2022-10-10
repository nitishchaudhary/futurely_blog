from contextlib import redirect_stderr
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'explore.html', {})
    else:
        return render(request, 'home.html', {})
        
    
