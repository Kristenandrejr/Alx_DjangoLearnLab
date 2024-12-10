from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegistrationView, UserProfileView

urlpatterns = [
    # Route for user registration
    path('register/', UserRegistrationView.as_view(), name='register'),

    # Route for user login
    path('login/', obtain_auth_token, name='login'),

    # Route for user profile management
    path('profile/', UserProfileView.as_view(), name='profile'),
]
