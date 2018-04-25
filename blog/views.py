from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects
    return render(request, 'blog/home.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post':post})
