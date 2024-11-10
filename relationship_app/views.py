from django.http import JsonResponse
from .models import Book

def list_books(request):
    books = Book.objects.all()  # Get all books
    book_list = [{"title": book.title, "author": book.author} for book in books]  # Extract titles and authors
    return JsonResponse({"books": book_list})

from django.http import JsonResponse
from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'

    def render_to_response(self, context, **kwargs):
        library = context['library']
        books = [{"title": book.title} for book in library.books.all()]  # List books in the library
        return JsonResponse({"library": library.name, "books": books})
