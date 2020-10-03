from django.urls import path
from .views import api_post_detail

urlpatterns = [
    path('<int:id>/', api_post_detail, name='det')
]