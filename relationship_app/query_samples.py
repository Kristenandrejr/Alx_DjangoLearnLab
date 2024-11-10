from relationship_app.models import Book, Author, Librarian

# List all books in a library
def list_books_in_library(library_name):
    books = Book.objects.filter(library_name=library_name)
    return books

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    librarian = Librarian.objects.filter(library_name=library_name).first()
    return librarian
