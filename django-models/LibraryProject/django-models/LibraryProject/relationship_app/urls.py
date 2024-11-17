from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Books and Library Details
    path('books/', list_books, name='list_books'),  # Function-based view to list all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details

    # Custom Authentication Views
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Custom login view
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),  # Custom logout view
    
    # Built-in Authentication Views (optional, if you need alternative login/logout)
    path('login_builtin/', LoginView.as_view(template_name='relationship_app/login.html'), name='login_builtin'),  # Built-in login view
    path('logout_builtin/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout_builtin'),  # Built-in logout view
    
    # Registration and Home views
    path('register/', views.register, name='register'),  # User registration view
    path('home/', views.home, name='home'),  # Home page view

    # Role-based views (secure views for specific roles)
    path('admin/', admin_view, name='admin_view'),  # Admin view (only accessible by Admin users)
    path('librarian/', librarian_view, name='librarian_view'),  # Librarian view (only accessible by Librarian users)
    path('member/', member_view, name='member_view'),  # Member view (only accessible by Member users)

    # Permissions-based views for managing books (add, edit, delete)
    path('add_book/', views.add_book, name='add_book'),  # Add a new book (permission required)
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # Edit a book (permission required)
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # Delete a book (permission required)
]
