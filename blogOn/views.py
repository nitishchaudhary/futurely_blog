from contextlib import redirect_stderr
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Blog
from django.contrib.auth import authenticate

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        loggedInId = request.user.id
        loggedInUser = User.objects.get(id = loggedInId)
        userBlogs = Blog.objects.filter(user = loggedInUser).order_by('-datePosted')
        
        return render(request, 'explore.html', {'userBlogs':userBlogs})
    else:
        return render(request, 'home.html', {})

def blogDetail(request, pk):
    blog = Blog.objects.get(id = pk)
    return render(request, 'blogDetail.html', {'blog':blog})

        
    
