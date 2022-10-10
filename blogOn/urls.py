from django.urls import path
from blogOn import views

urlpatterns = [
    path('', views.home, name = 'home'),
]