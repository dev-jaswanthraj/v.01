from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Post


def allowed_user(view_fun):
    def wrapper_func(request, *args, **kwargs):
        dct = kwargs
        post_user = Post.objects.get(id = dct['id']).cust
        if request.user == post_user:
            return view_fun(request, *args, **kwargs)
        else:
            return render(request, '404.html')
    return wrapper_func