# relationship_app/views.py

from django.shortcuts import render
from .models import Book
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library

def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    print(books)  # Debugging line to check the books fetched

    # Render the template and pass the books
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
