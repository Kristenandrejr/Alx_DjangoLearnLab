from django.urls import path
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view  # Explicitly import the function-based and class-based views
from django.contrib.auth.views import LoginView, LogoutView  # Import LoginView and LogoutView

urlpatterns = [
    # Books and Library Details
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view

    # Custom Authentication Views
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    
    # Built-in Authentication Views (For Savanna check)
    path('login_builtin/', LoginView.as_view(template_name='relationship_app/login.html'), name='login_builtin'),
    path('logout_builtin/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout_builtin'),
    
    # Registration and Home views
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    
    # Role-based views
    path('admin/', admin_view, name='admin_view'),  # Admin view
    path('librarian/', librarian_view, name='librarian_view'),  # Librarian view
    path('member/', member_view, name='member_view'),  # Member view
]
