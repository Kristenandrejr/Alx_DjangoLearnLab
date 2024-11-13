from django.urls import path
from . import views  # Import your views
from django.contrib.auth.views import LoginView, LogoutView  # Import LoginView and LogoutView

# Ensure 'list_books' is available in views
urlpatterns = [
    # Books and Library Details
    path('books/', views.list_books, name='list_books'),  # This is fine, 'list_books' is accessed via 'views'
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Custom Authentication Views
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    
    # Built-in Authentication Views (For Savanna check)
    path('login_builtin/', LoginView.as_view(template_name='relationship_app/login.html'), name='login_builtin'),
    path('logout_builtin/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout_builtin'),
    
    # Registration and Home views
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
]

