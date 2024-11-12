from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the list_books.html template with the books context
    return render(request, 'list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Define the template to render
    context_object_name = 'library'  # The context variable passed to the template
