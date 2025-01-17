from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# View to list all books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Example view to handle the form
def example_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            publication_year = form.cleaned_data["publication_year"]
            # You can save this data to the database or perform other actions
            return render(request, "bookshelf/success.html", {"title": title})
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})
