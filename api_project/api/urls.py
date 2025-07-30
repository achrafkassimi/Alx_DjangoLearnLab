from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create and register the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
# print("Router registered with basename 'book_all'",router)

urlpatterns = [
    # ListAPIView for the /books/ endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Router-generated endpoints for full CRUD
    path('', include(router.urls)),
]
