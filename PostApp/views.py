from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.


def index(request):
    posts=Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html',context)


def blog(request):
   posts=Post.objects.all()
   context = {'posts': posts}
   return render(request, 'posts/blog.html', context)
