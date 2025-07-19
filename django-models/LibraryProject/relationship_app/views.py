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
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # this is the object you'll refer to in your template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        
        # Fetch books related to the library directly via the ManyToMany relationship
        context['books_list'] = library.books.all()
        
        return context
