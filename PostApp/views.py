from django.shortcuts import render, HttpResponse,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .forms import PostForm
from django.contrib.auth.models import User


def index(request):
    posts = Post.objects.order_by('-date_posted')[:4]
    context = {'posts': posts}
    return render(request, 'index.html', context)


class PostListView(ListView):
    model = Post
    template_name = "posts/blog.html"
    queryset = Post.objects.filter(is_published=True)
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by=3

class UserPostListView(ListView):
    model = Post
    template_name = "posts/user_blog.html"
    context_object_name = "posts"
    paginate_by=3

    def get_query_set(self):
        user =get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user,is_published=True).order_by('-date_posted')




class PostDetailView(DetailView):
    model = Post
    template_name = "posts/blog_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    template_name = "posts/blog_create.html"


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    template_name = "posts/blog_create.html"


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    template_name="posts/blog_delete.html"

# def blog(request):
#    posts=Post.objects.all()
#    context = {'posts': posts}
#    return render(request, 'posts/blog.html', context)
