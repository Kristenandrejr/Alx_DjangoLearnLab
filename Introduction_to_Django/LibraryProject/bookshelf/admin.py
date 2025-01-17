from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality for title and author fields
    search_fields = ('title', 'author')
    
    # Enable filtering by publication year
    list_filter = ('publication_year',)
