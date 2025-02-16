from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, UserUpdateForm, ProfilePictureForm
from .models import UserProfile



def get_or_create_user_profile(user):
    profile, created = UserProfile.objects.get_or_create(user=user)
    return profile

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)  # Create profile for user
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    user_profile = get_or_create_user_profile(request.user)
    return render(request, 'profile.html', {'user': request.user, 'user_profile': user_profile})

@login_required
def edit_profile(request):
    user_profile = get_or_create_user_profile(request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfilePictureForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfilePictureForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

