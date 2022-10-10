from django.urls import path
from blogOn import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('blog_id=<int:pk>', views.blogDetail, name = 'blogDetail'),
    path('comment_id=<int:pk>', views.comment, name = 'comment'),
    path('sharePost_id=<int:pk>', views.sharePost, name = 'sharePost'),
]