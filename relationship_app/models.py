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
<<<<<<< HEAD
    library_name = models.CharField(max_length=100)

    def __str__(self):
<<<<<<< HEAD
        return f"{self.name} at {self.library_name}"
=======
        return self.name
>>>>>>> d5fd5adc1b87251729b840f3145415bb0e655970
=======
    library = models.CharField(max_length=100)
>>>>>>> c02058f04dfc8336a35a6571e2e3f95e094b3df3
