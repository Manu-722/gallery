from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import SignUpForm, ProfileUpdateForm

User = get_user_model()

def signup_view(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('gallery:home')
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('gallery:home')
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def edit_profile_view(request):
    form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('users:profile')
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def change_password_view(request):
    form = PasswordChangeForm(user=request.user, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('users:profile')
    return render(request, 'password_change.html', {'form': form})