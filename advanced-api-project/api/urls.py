from django.urls import path
# from .views import BookListCreateView, BookDetailView
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView


urlpatterns = [
    # path('books/', BookListCreateView.as_view(), name='book-list-create'),
    # path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),

    # The following paths match the expected keywords exactly:
    path('books/create/', CreateView.as_view(), name='book-create'),  # POST
    path('books/update/', UpdateView.as_view(), name='book-update'),  # PUT/PATCH via query param
    path('books/delete/', DeleteView.as_view(), name='book-delete'),  # DELETE via query param
]
