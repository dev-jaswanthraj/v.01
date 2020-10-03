from django.urls import path
from . import views
from posts.views import post_home

urlpatterns = [
    path('',views.home, name = 'home'),
    path('posts/', post_home, name = 'main'),
]