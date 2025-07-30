from django.shortcuts import render

# Create your views List All Books.
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import IsAuthenticatedOrReadOnly



class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Create your views BookViewSet.
# ViewSet to handle all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]

