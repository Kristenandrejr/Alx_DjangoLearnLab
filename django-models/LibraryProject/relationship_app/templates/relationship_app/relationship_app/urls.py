from django.urls import path
<<<<<<< Updated upstream
from . import views

urlpatterns = [
    # URL for adding a book
    path('add_book/', views.add_book, name='add_book'),

    # URL for editing a book
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),

    # URL for deleting a book
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    # Other URL patterns (e.g., list_books, library detail)
    path('list_books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
=======
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view  # Explicitly import the function-based and class-based views
from django.contrib.auth.views import LoginView, LogoutView  # Import LoginView and LogoutView

urlpatterns = [
    # Books and Library Details
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
>>>>>>> Stashed changes

    # Custom Authentication Views
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    
    # Built-in Authentication Views
    path('login_builtin/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login_builtin'),
    path('logout_builtin/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout_builtin'),
    
    # Registration and Home views
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    
    # Role-based views
    path('admin/', admin_view, name='admin_view'),  # Admin view
    path('librarian/', librarian_view, name='librarian_view'),  # Librarian view
    path('member/', member_view, name='member_view'),  # Member view
]
