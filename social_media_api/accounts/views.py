from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model

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
