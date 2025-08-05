# from rest_framework import generics, permissions
# from .models import Book
# from .serializers import BookSerializer
# from rest_framework import filters
# from .permissions import IsAdminOrReadOnly
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# # List all books or create a new one
# class BookListCreateView(generics.ListCreateAPIView):
#     """
#     GET: List all books (public)
#     POST: Create a new book (authenticated users only)
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'publication_year']

#     permission_classes = [IsAdminOrReadOnly]


#     # Allow only authenticated users to POST
#     def get_permissions(self):
#         if self.request.method == 'POST':
#             return [permissions.IsAuthenticated()]
#         return [permissions.AllowAny()]
    
#     def perform_create(self, serializer):
#         # Example: force assign a default author (e.g., ID = 1)
#         default_author = self.request.user.author_profile  # If you connect User to Author
#         serializer.save(author=default_author)

# # Retrieve, update, or delete a book
# class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     # Restrict PUT, PATCH, DELETE to authenticated users
#     def get_permissions(self):
#         if self.request.method in ['PUT', 'PATCH', 'DELETE']:
#             return [permissions.IsAuthenticated()]
#         return [permissions.AllowAny()]



# # ListView: List all books
# class ListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.AllowAny]

# # DetailView: Get one book
# class DetailView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.AllowAny]

# # CreateView: Add a new book
# class CreateView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]

# # # UpdateView: Modify a book
# # class UpdateView(generics.UpdateAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer
# #     permission_classes = [permissions.IsAuthenticated]

# # # DeleteView: Delete a book
# # class DeleteView(generics.DestroyAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer
# #     permission_classes = [permissions.IsAuthenticated]

# class UpdateView(generics.UpdateAPIView):
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self):
#         book_id = self.request.query_params.get('id')
#         return Book.objects.get(pk=book_id)

# class DeleteView(generics.DestroyAPIView):
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self):
#         book_id = self.request.query_params.get('id')
#         return Book.objects.get(pk=book_id)

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny  # ✅ Explicit import

from .models import Book
from .serializers import BookSerializer


# GET all books — open to anyone
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # ✅ Public access


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
