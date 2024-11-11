import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"No author found with the name: {author_name}"

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return f"No library found with the name: {library_name}"

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return f"No library found with the name: {library_name}"
    except Librarian.DoesNotExist:
        return "This library does not have a librarian assigned."

# Example usage
if __name__ == "__main__":
    print(get_books_by_author("Author Name"))
    print(get_books_in_library("Library Name"))
    print(get_librarian_for_library("Library Name"))
