# relationship_app/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Librarian(models.Model):
    name = models.CharField(max_length=100)

class Library(models.Model):
    name = models.CharField(max_length=100)
    librarian = models.OneToOneField(Librarian, on_delete=models.CASCADE, related_name='library')
    books = models.ManyToManyField(Book, related_name='libraries')