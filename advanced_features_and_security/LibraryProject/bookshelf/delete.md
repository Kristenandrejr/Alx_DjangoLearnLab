# Delete a Book Instance

from bookshelf.models import Book

# Retrieve the book instance:
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance:
book.delete()
# Expected output:
# Confirmation that the book has been deleted.
