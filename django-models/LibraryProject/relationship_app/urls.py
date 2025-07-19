# relationship_app/urls.py

from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    # User authentication URLs
    # path('login/', views.login_view, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
]
