from django.db import models

class Author(models.Model):
    # Author model stores the author's name.
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Book model stores the title, publication year, and the relationship to the author.
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title