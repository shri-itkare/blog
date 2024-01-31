# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog1/home.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog1/create_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = PostForm(instance=post)
        return render(request, 'blog1/edit_post.html', {'form': form})
    else:
        return redirect('home')

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
    return redirect('home')

def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog1/view_post.html', {'post': post})
