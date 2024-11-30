# Advanced API Project

A Django REST Framework project for managing books and authors, demonstrating the use of custom views, generic views, serializers, and permissions.

## Features
- CRUD operations for books.
- Validation to ensure no future publication years.
- Permissions to differentiate access for authenticated and unauthenticated users.

## API Endpoints

### Books
- `GET /books/` - List all books
- `GET /books/<id>/` - Retrieve a specific book
- `POST /books/add/` - Add a new book
- `PUT /books/<id>/edit/` - Update a book
- `DELETE /books/<id>/delete/` - Delete a book

### Permissions
- **Unauthenticated Users**: Can only retrieve data (`GET` requests).
- **Authenticated Users**: Can create, update, and delete books.

## Getting Started

### Prerequisites
- Python 3.x
- Django
- Django REST Framework

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/advanced_api_project.git


   ### **README.md: API Query Features**

#### **Books API Endpoints**

*   **Filter by fields**:
    *   `/api/books/?author=John Doe` - Filter books by author.
    *   `/api/books/?publication_year=2023` - Filter books by publication year.
*   **Search**:
    *   `/api/books/?search=Python` - Search for books with "Python" in the title or author fields.
*   **Ordering**:
    *   `/api/books/?ordering=title` - Order books by title (ascending).
    *   `/api/books/?ordering=-publication_year` - Order books by publication year (descending).

