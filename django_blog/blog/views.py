# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

# User Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user and create the account
            login(request, user)  # Log the user in after successful registration
            return redirect('profile')  # Redirect to the profile page after registration
    else:
        form = CustomUserCreationForm()  # If GET request, show an empty form
    return render(request, 'blog/register.html', {'form': form})  # Render the register template with the form

# User Login View
def user_login(request):
    if request.method == 'POST':  # If POST request, authenticate the user
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in if credentials are correct
            return redirect('profile')  # Redirect to the profile page after successful login
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid credentials'})  # Show error message for invalid credentials
    return render(request, 'blog/login.html')  # If GET request, show the login form

# User Logout View
def user_logout(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to login page after logout

# User Profile View (Requires login)
@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})  # Show the user's profile page if authenticated
