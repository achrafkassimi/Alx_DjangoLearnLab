from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# BookSerializer serializes all Book fields and ensures publication_year is not in the future.
# AuthorSerializer nests BookSerializer to return the author's books as a list.
# The related_name='books' on the ForeignKey allows accessing books from an author instance.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
