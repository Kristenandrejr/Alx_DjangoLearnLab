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
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Corrected URL
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment management URLs
    path('post/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comments/<int:comment_id>/edit/', edit_comment, name='edit-comment'),
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete-comment'),
]
