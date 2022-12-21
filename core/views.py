from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html' , context,)

def detail(request, slug):
    post = Post.objects.get(slug = slug)
    context = {
        'post': post
    }
    return render(request, 'detail.html' , context,)