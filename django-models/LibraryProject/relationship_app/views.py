# relationship_app/views.py

from django.shortcuts import render
from .models import Book
from django.shortcuts import render
# from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Library

def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    # print(books)  # Debugging line to check the books fetched

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


# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirect to a home or dashboard page after login
    else:
        form = AuthenticationForm()

    return render(request, 'relationship_app/login.html', {'form': form})

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})

# relationship_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Check if the user is an admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if the user is a librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if the user is a member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
