from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
=======
from django.views.generic.detail import DetailView
from .models import Library, Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
>>>>>>> 355626e26b7c8bf3c62b61091c06e279a10e45aa

# User registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
<<<<<<< HEAD
    return render(request, 'register.html', {'form': form})
=======

    return render(request, 'relationship_app/register.html', {'form': form})
>>>>>>> 355626e26b7c8bf3c62b61091c06e279a10e45aa

# User login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the homepage or dashboard after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User logout view
def logout_view(request):
    logout(request)  # Log the user out
    return render(request, 'logout.html')  # Redirect to the logout confirmation page
