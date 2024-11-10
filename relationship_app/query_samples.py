<<<<<<< HEAD
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
=======
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)

# List all books in a library
library = Library.objects.get(name="Library Name")
books_in_library = library.books.all()
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
library = Library.objects.get(name="Library Name")
librarian = Librarian.objects.get(library=library)
print(f"Librarian: {librarian.name}")
>>>>>>> d5fd5adc1b87251729b840f3145415bb0e655970
