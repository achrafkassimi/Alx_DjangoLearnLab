from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView, CustomUserViewSet
from rest_framework.routers import DefaultRouter

# Set up a router for CustomUserViewSet
router = DefaultRouter()
router.register(r'users', CustomUserViewSet)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # Include follow/unfollow actions via CustomUserViewSet
    path('follow/<int:pk>/', CustomUserViewSet.as_view({'post': 'follow_user'}), name='follow_user'),
    path('unfollow/<int:pk>/', CustomUserViewSet.as_view({'post': 'unfollow_user'}), name='unfollow_user'),

    # Register the router URLs for the CustomUserViewSet
    path('', include(router.urls)),
]
