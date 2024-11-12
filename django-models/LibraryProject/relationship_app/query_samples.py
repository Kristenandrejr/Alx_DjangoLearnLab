from .models import Book, Author, Library, Librarian

# Query to list all books in a library
def list_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    return library.books.all()

# Query to get all books by a specific author
def books_by_author(author_id):
    return Book.objects.filter(author_id=author_id)

# Query to retrieve the librarian for a library
def librarian_for_library(library_id):
    return Librarian.objects.get(library_id=library_id)
