from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # Import Token model for token generation
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

# Custom User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']  # Customize this as per your model
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)  # Hash password
        user.save()
        Token.objects.create(user=user)  # Create a token for the user
        return user

# Custom User Login Serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Invalid credentials')

        # Generate a token for successful authentication
        token, _ = Token.objects.get_or_create(user=user)
        return {'token': token.key}
