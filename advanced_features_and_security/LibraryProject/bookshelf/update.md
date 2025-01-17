```python

>>> from bookshelf.models import Book
>>> book1 = Book.objects.get(pk=1) #retrieving book to be updated 
>>> book1 #confirming that correct book was retrieved
#output: <Book: '1984' by George Orwell>
>>> book.title = 'Nineteen Eighty-Four' #updating title field
>>> Book1
#output: <Book: 'Nineteen Eighty-Four' by George Orwell>
>>> book1.save() #saving the new changes to db
>>> Book.objects.get(pk=1) #confirming that update was successful
#output: <Book: 'Nineteen Eighty-Four' by George Orwell>