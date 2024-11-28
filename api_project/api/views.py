from rest_framework.generics import ListAPIView  # Import generics.ListAPIView
from rest_framework import viewsets  # Import viewsets (directly for clarity)
from rest_framework.permissions import IsAuthenticated, BasePermission  # Import permissions
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer


# A ListAPIView to list all books
class BookList(ListAPIView):
    """
    A view that provides a list of all books.
    """
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer for JSON serialization


# Custom permission to allow only admins to edit, but read access for everyone
class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admins to edit, but read access for everyone.
    """

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True  # Allow read-only access
        return request.user and request.user.is_staff  # Allow modifications only for admins


# A ModelViewSet to handle CRUD operations on the Book model with authentication and permissions
class BookViewSet(viewsets.ModelViewSet):  # Exact usage of "viewsets.ModelViewSet"
    """
    A viewset that provides CRUD operations for the Book model with authentication and custom permissions.
    """
    queryset = Book.objects.all()  # Query all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer for serialization
    permission_classes = [IsAuthenticated & IsAdminOrReadOnly]  # Authentication and custom permissions
