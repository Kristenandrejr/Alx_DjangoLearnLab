```python

>>> from bookshelf.models import Book
>>> Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
#output: <Book: '1984' by George Owrell>
>>> Book.objects.all()
#output: <Queryset [<Book: '1984' by George Orwell>,]>
>>> Book.objectives.values_list('pk', 'title')
#output: <Queryset [(2,)]>
>>> book1 = Book.objects.get(pk=2)
>>> book1
#output: <Book: '1984' by George Orwell>
>>> book1.title
'1984'
>>> book1.author
'George Orwell'
>>> book1.publication_year
'1949'
>>> book1.title = 'nineteen Eighty-Four'
>>>book1
#output: <Book: 'Nineteen Eighty-Four' by George Orwell>
>>> book1.save()
>>> Book.objects.get(pk=2)
#output: <Book: 'nineteen Eighty-Four' by George Orwell>
>>> book1.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
#output: <Queryset []>
