# Delete Operation

## Command
from bookshelf.models import Book  # Importing the Book model
book = Book.objects.first()
book.delete()
print(Book.objects.all())

# Documents
```python
book = Book.objects.first()
book.delete()
print(Book.objects.all())

# Expected Output
<QuerySet []>
