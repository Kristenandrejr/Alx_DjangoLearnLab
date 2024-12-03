from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CustomUserCreationForm
from .models import Post

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
    if request.method == 'POST':  # Handle form submission to update email
        request.user.email = request.POST['email']  # Update the user's email
        request.user.save()  # Save the updated user instance
        return redirect('profile')  # Redirect to the profile page after saving changes

    return render(request, 'blog/profile.html', {'user': request.user})  # Render the user's profile page if GET request

# Blog Post Management Views
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # HTML file
    context_object_name = 'posts'
    ordering = ['-published_date']  # Use your original model's field

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
