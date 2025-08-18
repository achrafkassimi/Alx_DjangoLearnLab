from django.urls import path, include
from .views import FollowUserView, RegisterView, LoginView, ProfileView, CustomUserViewSet, UnfollowUserView
from rest_framework.routers import DefaultRouter

# Set up a router for CustomUserViewSet
router = DefaultRouter()
router.register(r'users', CustomUserViewSet)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # Follow and Unfollow routes
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow_user'),

    # Register the router URLs for the CustomUserViewSet
    # path('', include(router.urls)),s
]
