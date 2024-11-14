# Retrieve a Book Instance

# Command to retrieve the book created earlier by title:
book = Book.objects.get(title="1984")
# Expected output:
# Book(title='1984', author='George Orwell', publication_year=1949)
