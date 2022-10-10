from platform import release
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, related_name = "blog", on_delete = models.CASCADE)
    title = models.CharField(max_length=255, default="")
    description = models.TextField()
    datePosted = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs = {'pk':self.pk})

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name = "comments", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name = "comments", on_delete = models.CASCADE)
    email = models.CharField(max_length=255, default="")
    comment = models.TextField()
    commentDate = models.DateTimeField(default = timezone.now)