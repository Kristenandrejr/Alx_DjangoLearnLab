# Retrieve Operation
## Using `Book.objects.get()`

## Command
book = Book.objects.first()
print(book.title, book.author, book.publication_year)

# documents 

```python
book = Book.objects.first()
print(book.title, book.author, book.publication_year)

# Expected Output
1984 George Orwell 1949



