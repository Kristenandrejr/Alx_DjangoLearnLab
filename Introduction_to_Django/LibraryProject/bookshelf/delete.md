# Delete Operation

## Command
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
