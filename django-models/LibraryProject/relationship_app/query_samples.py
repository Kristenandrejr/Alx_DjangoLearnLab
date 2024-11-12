from .models import Library, Author, Librarian

def list_books_in_library(library_name):
    # Retrieves a library by name and lists all its books
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Assumes `books` is a ManyToManyField in Library
    return books

def query_books_by_author(author_name):
    # Retrieves all books by a specific author
    author = Author.objects.get(name=author_name)
    books = author.book_set.all()  # Retrieves related books for the author
    return books

def retrieve_librarian_for_library(library_name):
    # Retrieves the librarian for a specific library
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Assumes `Librarian` has a OneToOneField with Library
    return librarian
