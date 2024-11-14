from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

# View to add a book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # Your code for adding a book goes here
    return render(request, 'add_book.html')

# View to edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Your code for editing a book goes here
    return render(request, 'edit_book.html', {'book': book})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Your code for deleting a book goes here
    return render(request, 'delete_book.html', {'book': book})

