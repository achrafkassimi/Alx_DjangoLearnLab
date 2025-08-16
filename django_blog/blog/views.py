from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# blog/views.py (Add this to your profile view)
from .models import UserProfile

# User Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        # Update email
        request.user.email = request.POST['email']
        request.user.save()

        # Update profile information
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_profile.bio = request.POST.get('bio', user_profile.bio)
        if 'profile_picture' in request.FILES:
            user_profile.profile_picture = request.FILES['profile_picture']
        user_profile.save()

        messages.success(request, "Profile updated successfully.")
    return render(request, 'blog/profile.html', {'user_profile': UserProfile.objects.get(user=request.user)})


# blog/views.py

from django.shortcuts import render

def home(request):
    # This will render the home.html template when you visit the root URL.
    return render(request, 'blog/home.html')
