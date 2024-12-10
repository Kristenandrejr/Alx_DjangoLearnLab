from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegistrationView, UserProfileView, follow_user, unfollow_user

urlpatterns = [
    # Route for user registration
    path('register/', UserRegistrationView.as_view(), name='register'),

    # Route for user login
    path('login/', obtain_auth_token, name='login'),

    # Route for user profile management
    path('profile/', UserProfileView.as_view(), name='profile'),

    # Route for following a user
    path('follow/<int:user_id>/', follow_user, name='follow_user'),

    # Route for unfollowing a user
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]
