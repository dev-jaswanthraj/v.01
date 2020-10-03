from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, Http404
from .models import *
from .forms import PostForm
from django.db.models.signals import pre_save
from django.contrib import messages
from django.contrib.auth.models import User
from .decorators import allowed_user
from .forms import CreateForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/posts/login')
def post_home(request):
    top_10_post = Post.objects.all()
    u = False
    if request.user.is_staff or request.user.is_superuser:
        u = True
    if request.method == "POST":
        name = request.POST.get('username')
        user_profile = User.objects.filter(username__icontains=name)
        context = {
            'user_prof':user_profile,
            'top_10_post':top_10_post,
            'u':u
        }
        return render(request,'post_home.html',context)
    context = {
        'top_10_post':top_10_post,
    }
    return render(request,'post_home.html',context)
@login_required(login_url='/posts/login')
def post_create(request):
    cust = User.objects.get(username = request.user)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.cust = cust
            instance.save()
            title = form.cleaned_data.get('title')
            messages.success(request, "The "+title+" Post Was Saved!")
            return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form':form
    }
    return render(request, 'post_form.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id = id)
    context = {
        'post':post
    }
    return render(request, 'post_detail.html', context)

def post_list(request, id):
    u = User.objects.get(id = id)
    query= Post.objects.filter(cust = u)#.order_by('-timestamp')
    context = {
        'queryset': query,
    }
    return render(request, 'post_list.html', context)
@allowed_user
def post_update(request, id):
    if not request.user.is_staff or not request.user.is_superuser:
        return render(request, '404.html')
    post = get_object_or_404(Post, id = id)
    form = PostForm(instance= post)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance = post)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.save()
            title = form.cleaned_data.get('title')
            messages.success(request, "The "+title+" Post Was Updated!")
            return HttpResponseRedirect(instance.get_absolute_url())  
    context = {
        'post':post,
        'form':form
    }
    return render(request, 'post_form.html', context)
@allowed_user
def post_delete(request, id):
    if not request.user.is_staff or not request.user.is_superuser:
        return render(request, '404.html')
    post = get_object_or_404(Post, id = id)
    post.delete()
    messages.success(request, 'The Post is Successfuly Deleted!!')
    return redirect('post_list')

def register(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            print('Some Thing Wrong')
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, 'Account is created to '+name)
            return redirect('/login')
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/posts/')
        else:
            messages.info(request, 'The username or passwprd is incorrect')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')
