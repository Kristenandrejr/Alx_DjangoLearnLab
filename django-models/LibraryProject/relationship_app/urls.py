from django.urls import path
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

    # Custom Authentication Views
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    
    # Built-in Authentication Views
    path('login_builtin/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login_builtin'),
    path('logout_builtin/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout_builtin'),
    
    # Registration and Home views
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
]
