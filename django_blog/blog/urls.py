from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment, 
    edit_comment, 
    delete_comment,
    PostByTagListView,  # Import the view for posts by tag
)

urlpatterns = [
    # Original user authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    # Blog post management URLs
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment management URLs
    path('post/<int:pk>/comments/new/', add_comment, name='add-comment'),  # This was missing
    path('comment/<int:pk>/update/', edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete-comment'),

    # New URL pattern for filtering posts by tag
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post-by-tag'),
]
