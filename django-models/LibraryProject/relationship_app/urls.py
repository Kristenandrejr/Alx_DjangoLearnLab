from django.urls import path
from . import views  # Import your views
from django.contrib.auth.views import LoginView, LogoutView  # Import LoginView and LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    
    # Home view after login
    path('home/', views.home, name='home'),
]
