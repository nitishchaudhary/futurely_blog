from contextlib import redirect_stderr
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Blog, Comment
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        loggedInId = request.user.id
        loggedInUser = User.objects.get(id = loggedInId)
        userBlogs = Blog.objects.filter(user = loggedInUser).order_by('-datePosted')
        paginator = Paginator(userBlogs, 5)
        page_number = request.GET.get('page')
        try:
            page_obj = paginator.get_page(page_number) 
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        
        return render(request, 'explore.html', {'page_obj':page_obj})
    else:
        return render(request, 'home.html', {})

def blogDetail(request, pk):
    if request.user.is_authenticated:
        blog = Blog.objects.get(id = pk)
        blogComments = Comment.objects.filter(blog = blog)
        return render(request, 'blogDetail.html', {'blog':blog, 'blogComments':blogComments})
    else:
        return redirect('/')

def comment(request, pk):
    if request.user.is_authenticated:
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
        return redirect('/')

def sharePost(request, pk):
    if request.user.is_authenticated:
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

    else:
        return redirect('/')

def writeBlog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            loggedInId = request.user.id
            loggerInUser = User.objects.get(id = loggedInId)
            title = request.POST['title']
            content = request.POST['blogContent']
            blogObj = Blog.objects.create(user = loggerInUser, title = title, description = content)
            blogObj.save()
            return redirect('/')
        elif request.method == "GET":
            return render(request, 'writeBlog.html', {})
            
    else:
        return redirect('/')

