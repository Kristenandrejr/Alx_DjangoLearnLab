from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField()

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} at {self.library_name}"
        return self.name
    library = models.CharField(max_length=100)
