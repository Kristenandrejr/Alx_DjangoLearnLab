from rest_framework.generics import ListAPIView  # Import generics.ListAPIView
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer

class BookList(ListAPIView):
    """
    A view that provides a list of all books.
    """
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer for JSON serialization
