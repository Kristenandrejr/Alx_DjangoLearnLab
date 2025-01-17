# Update Operation

# Command
book = Book.objects.first()
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

# Document
```python
book = Book.objects.first()
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

# Expected Output
Nineteen Eighty-Four by George Orwell (1949)
