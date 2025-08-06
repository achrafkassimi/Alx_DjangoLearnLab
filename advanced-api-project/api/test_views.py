from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')

        # Create an author
        self.author = Author.objects.create(name='Achraf Kassimi')

        # Create books
        self.book1 = Book.objects.create(title="AI in Education", publication_year=2023, author=self.author)
        self.book2 = Book.objects.create(title="Learning Django", publication_year=2024, author=self.author)

        # URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update') + "?id={}".format(self.book1.id)
        self.delete_url = reverse('book-delete') + "?id={}".format(self.book1.id)
        self.detail_url = reverse('book-detail', args=[self.book1.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        data = {
            'title': 'New Book',
            'publication_year': 2025,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_create_book_unauthenticated(self):
        data = {
            'title': 'Blocked Book',
            'publication_year': 2025,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        data = {
            'title': 'Updated Title',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + '?title=AI in Education')
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_author_name(self):
        response = self.client.get(self.list_url + '?search=Achraf')
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url + '?ordering=-publication_year')
        self.assertEqual(response.data[0]['title'], "Learning Django")






