from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 Home page
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Blog Post CRUD URLs
    path('posts/', views.PostListView.as_view(), name='post_list'),  # List all posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # View single post
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # Create new post
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # Edit post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete post
]
