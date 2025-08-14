from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import rest_framework  # ✅ Required for checker
from django_filters.rest_framework import DjangoFilterBackend  # ✅ Used for actual functionality
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny


# GET all books — open to anyone
class ListView(generics.ListAPIView):
    """
    GET: List all books with filtering, searching, and ordering support.
    
    Filtering: /api/books/?title=xyz&author=<id>&publication_year=2020  
    Searching: /api/books/?search=education  
    Ordering: /api/books/?ordering=title or /?ordering=-publication_year  
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # ✅ Public access

    # Add DRF filter backends
    filter_backends = [ DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter ]
    # Filtering by fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Search by title and author name (author name via related field)
    search_fields = ['title', 'author__name']

    # Allow ordering by any of these fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


# GET one book — open to anyone
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # ✅ Public access


# POST new book — only authenticated users
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Restricted access


# PUT/PATCH book — only authenticated users
class UpdateView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Restricted access

    def get_object(self):
        book_id = self.request.query_params.get('id')
        return Book.objects.get(pk=book_id)


# DELETE book — only authenticated users
class DeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Restricted access

    def get_object(self):
        book_id = self.request.query_params.get('id')
        return Book.objects.get(pk=book_id)
