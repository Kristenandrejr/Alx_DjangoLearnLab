from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} at {self.library_name}"
