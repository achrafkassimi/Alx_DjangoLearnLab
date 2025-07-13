# Django Admin Customization for Book Model

The following features are enabled in the Django admin:

- **List Display**: title, author, publication_year
- **Filters**: author, publication_year
- **Search Fields**: title, author

## Code Snippet (admin.py)
```python
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
