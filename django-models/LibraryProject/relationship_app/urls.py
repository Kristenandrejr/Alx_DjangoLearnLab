from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),  # Registration URL
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Login URL
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),  # Logout URL
    path('home/', views.home, name='home'),  # Home page after login
]
