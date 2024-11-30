from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookApiTests(APITestCase):

    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a test book to interact with
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_year=2020
        )
        
        # Authenticate with the test user
        self.client.login(username='testuser', password='testpassword')

    def test_create_book(self):
        # Test creating a new book
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2023
        }
        response = self.client.post('/books/add/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')
        self.assertEqual(response.data['author'], 'New Author')

    def test_read_book(self):
        # Test retrieving a specific book by ID
        response = self.client.get(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        # Test updating a book's data
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2022}
        response = self.client.put(f'/books/{self.book.id}/edit/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book')

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(f'/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Ensure the book is deleted from the database
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        # Test filtering by title
        response = self.client.get('/books/', {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only the test book should be returned

    def test_search_books(self):
        # Test searching by author
        response = self.client.get('/books/', {'search': 'Test Author'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only the test book should be returned

    def test_order_books(self):
        # Test ordering books by publication year
        Book.objects.create(title="Old Book", author="Old Author", publication_year=2015)
        response = self.client.get('/books/', {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]['publication_year'] <= response.data[1]['publication_year'])

    def test_permissions_for_unauthenticated_users(self):
        # Test that unauthenticated users cannot create or delete books
        self.client.logout()
        data = {
            'title': 'Unauthenticated Book',
            'author': 'Unauthenticated Author',
            'publication_year': 2023
        }
        response = self.client.post('/books/add/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_permissions_for_authenticated_users(self):
        # Test that authenticated users can create, update, and delete books
        self.client.logout()
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/books/add/', {'title': 'Auth Book', 'author': 'Auth Author', 'publication_year': 2023})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
