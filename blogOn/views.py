from asyncio.windows_events import NULL
from contextlib import redirect_stderr
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Blog, Comment
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings

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
    blogComments = Comment.objects.filter(blog = blog)
    return render(request, 'blogDetail.html', {'blog':blog, 'blogComments':blogComments})

def comment(request, pk):
    if request.method == "POST":
        loggedInId = request.user.id
        loggerInUser = User.objects.get(id = loggedInId)
        currentBlog = Blog.objects.get(id = pk)
        email = request.POST['email']
        commentData = request.POST['comment']
        commentObj = Comment.objects.create(user = loggerInUser, blog = currentBlog, email = email, comment = commentData)
        commentObj.save()
        return HttpResponse('Done')
    else:
        return NULL

def sharePost(request, pk):
    if request.method == "POST":
        currentBlog = Blog.objects.get(id = pk)
        username = request.POST['username']
        emailFrom = request.POST['emailFrom']
        emailTo = request.POST['emailTo']
        emailComments = request.POST['emailComments']
        if emailFrom and emailTo:
            send_mail(subject = currentBlog.title,
            message = currentBlog.description,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list= [emailTo]
            )

    elif request.method == "GET":
        currentBlog = Blog.objects.get(id = pk)
        if currentBlog is not None:
            return render(request, 'sharePost.html', {'blog':currentBlog})
        else:
            return redirect('/')
        
    
