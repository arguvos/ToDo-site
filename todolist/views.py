from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import PostForm
from todolist import forms
from .models import Task
from django.shortcuts import render, get_object_or_404

def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    tasks = Task.objects.all()
    form = PostForm()
    return render(request, "index.html", {
            'tasks': tasks,
            'form': form
        })

@login_required
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def edit(request, pk):
    form = PostForm(request.POST)        
    tasks = Task.objects.all(pk)
    form = PostForm(request.POST, instance=pk)
    form.save()
    return render(request, 'home.html')

def edit(request, pk, field_pk):
    post = get_object(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            print(post)            
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form})

def delete(request, pk):
    todofield = get_object_or_404(Task, pk=pk)
    todofield.delete()
    return render(request, 'home.html')