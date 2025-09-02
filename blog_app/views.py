from django.shortcuts import render 
from .models import Post

def get_all_post(request):
    posts=Post.objects.all()
    return render (request,'blog-app/blog.html',{
        'posts':posts
    })


def home(request):
    return render(request, 'blog-app/home.html')


       






