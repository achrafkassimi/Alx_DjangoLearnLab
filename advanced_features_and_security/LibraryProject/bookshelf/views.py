from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from advanced_features_and_security.LibraryProject.bookshelf.forms import SearchForm
from relationship_app.models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        # save logic here
        ...
    return render(request, 'book_form.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def book_edit(request, book_id):
    # logic to edit book
    ...

@permission_required('relationship_app.can_delete', raise_exception=True)
def book_delete(request, book_id):
    # logic to delete book
    ...


def search_books(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.none()
    return render(request, 'bookshelf/book_list.html', {'books': books})
