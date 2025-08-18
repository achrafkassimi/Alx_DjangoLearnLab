from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

# Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

# Login View
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'token': serializer.validated_data['token']})
        return Response(serializer.errors, status=400)

# Profile View (Authenticated)
class ProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]  # You can change this to a custom permission if you need

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            # 'email': user.email,
            # 'bio': user.bio,
            # 'profile_picture': user.profile_picture.url if user.profile_picture else None
        })



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow_user(self, request, pk=None):
        user_to_follow = self.get_object()
        user = request.user

        if user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        user.following.add(user_to_follow)  # Add to following
        return Response({"detail": f"Now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unfollow_user(self, request, pk=None):
        user_to_unfollow = self.get_object()
        user = request.user

        if user == user_to_unfollow:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        user.following.remove(user_to_unfollow)  # Remove from following
        return Response({"detail": f"Unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)



# accounts/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import CustomUser
from rest_framework import status
from .serializers import CustomUserSerializer

# View to handle following a user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user_to_follow = CustomUser.objects.get(id=pk)
        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)  # Add user to following
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

# View to handle unfollowing a user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user_to_unfollow = CustomUser.objects.get(id=pk)
        if user_to_unfollow == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)  # Remove user from following
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
