from rest_framework.generics import ListAPIView  # Import generics.ListAPIView
from rest_framework import viewsets.ModelViewSet  # Import viewsets (directly for clarity)
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer


# A ListAPIView to list all books
class BookList(ListAPIView):
    """
    A view that provides a list of all books.
    """
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer for JSON serialization


# A ModelViewSet to handle CRUD operations on the Book model
class BookViewSet(viewsets.ModelViewSet):  # Exact usage of "viewsets.ModelViewSet"
    """
    A viewset that provides CRUD operations for the Book model.
    """
    queryset = Book.objects.all()  # Query all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer for serialization
