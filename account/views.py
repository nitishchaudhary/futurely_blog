from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username = username, password = password)
            print(user)
            if user is not None:
                auth_login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('/')

        else:
            return redirect('/')

    else:
        return render(request, 'home.html', {})

def signUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if username and email and password:
            user = User.objects.create_user(username = username, email = email, password = password)
            if user is not None:
                user.save()
                auth_login(request, user)
                return redirect('/')
        else:
            return redirect('/')
            
    else:
        return redirect('/')

def logOut(request):
    logout(request)
    return redirect('/')