# relationship_app/query_samples.py
from .models import Book, Author, Library

def list_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    return library.books.all()

def list_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

def get_librarian_for_library(library_id):
    library = Library.objects.get(id=library_id)
    return library.librarian
