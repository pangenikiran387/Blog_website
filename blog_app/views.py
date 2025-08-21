from django.shortcuts import render

def blog_posts(request):
    return render (request,'blog-app/blog.html')
