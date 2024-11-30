from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # Added IsAuthenticated
import datetime
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    View to list all books.
    Unauthenticated users have read-only access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve details of a specific book by ID.
    Unauthenticated users have read-only access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book.
    Only authenticated users can create books.
    Validates that the publication year is not in the future.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Changed to IsAuthenticated for stricter permissions

    def perform_create(self, serializer):
        publication_year = serializer.validated_data.get('publication_year')
        if publication_year > datetime.date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.
    Only authenticated users can update books.
    Validates that the publication year is not in the future.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Changed to IsAuthenticated for stricter permissions

    def perform_update(self, serializer):
        publication_year = serializer.validated_data.get('publication_year')
        if publication_year > datetime.date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book.
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Changed to IsAuthenticated for stricter permissions
