from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    """
    A view that provides a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
