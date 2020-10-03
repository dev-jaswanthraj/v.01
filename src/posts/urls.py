from django.urls import path
from .views import (
    post_create,
    post_delete,
    post_detail,
    post_home,
    post_list, 
    post_update,
    register,
    login_page,
    logoutUser
)

urlpatterns = [
    path('home/', post_home, name = 'post_home'),
    path('create/', post_create, name = 'create'),
    path('<int:id>/update/', post_update, name = 'update'),
    path('<int:id>/delete/', post_delete, name = 'delete'),
    path('<int:id>/', post_detail, name = 'detail'),
    path('post_list/<int:id>/', post_list, name = 'post_list'),
    path('register/', register, name = 'reg'),
    path('login/', login_page, name = 'login'),
    path('logout/',logoutUser, name = 'logout')
]