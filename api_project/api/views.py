from rest_framework.generics import ListAPIView  # Import generics.ListAPIView
from rest_framework.viewsets import ModelViewSet  # Import ModelViewSet
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer


class BookList(ListAPIView):
    """
    A view that provides a list of all books.
    """
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer for JSON serialization


class BookViewSet(ModelViewSet):
    """
    A viewset that provides CRUD operations for the Book model.
    """
    queryset = Book.objects.all()  # Query all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer for serialization
