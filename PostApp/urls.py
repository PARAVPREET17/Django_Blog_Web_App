from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('blog',views.PostListView.as_view(),name='blog'),
    path('blog-detail/<int:pk>',views.PostDetailView.as_view(),name='blog-detail'),
    path('blog-update/<int:pk>',views.PostUpdateView.as_view(),name='blog-update'),
    path('blog-delete/<int:pk>',views.PostDeleteView.as_view(),name='blog-delete'),
    path('blog-add',views.PostCreateView.as_view(),name='blog-add'),
]
