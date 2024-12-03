from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q  # Importing Q objects for complex queries
from .forms import CustomUserCreationForm, CommentForm
from .models import Post, Comment

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

# Comment Functionality (Class-Based Views for CRUD)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('post-detail', pk=self.kwargs['post_id'])

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def get_object(self):
        return get_object_or_404(Comment, id=self.kwargs['comment_id'], author=self.request.user)

    def get_success_url(self):
        return redirect('post-detail', pk=self.object.post.id)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def get_object(self):
        return get_object_or_404(Comment, id=self.kwargs['comment_id'], author=self.request.user)

    def get_success_url(self):
        return redirect('post-detail', pk=self.object.post.id)

# Comment Functionality (Function-Based Views)
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        post_id = comment.post.id
        comment.delete()
        return redirect('post-detail', pk=post_id)
    return render(request, 'blog/delete_comment.html', {'comment': comment})

# Search Functionality
def search(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) |
        Q(tags__name__icontains=query)  # Filter by title, content, or tags
    ).distinct()
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})  # Render the search results

