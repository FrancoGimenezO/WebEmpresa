from django.shortcuts import render
from .models import Category, Post

def blogs(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'categories': categories, 'posts': posts})
