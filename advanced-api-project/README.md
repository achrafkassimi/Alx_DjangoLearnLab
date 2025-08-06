- (venv) C:\Users\melua\Documents\Alx_DjangoLearnLab\advanced-api-project>python manage.py createsuperuser
Username (leave blank to use 'achraf'): achraf
Email address: achraf@gmail.com
Password: 1234
Password (again): 1234
- venv\Scripts\activate.bat

## API Endpoints

### Books
- `GET /api/books/` — List all books
- `POST /api/books/` — Create a new book (authenticated)
- `GET /api/books/<id>/` — Retrieve a specific book
- `PUT /api/books/<id>/` — Update a book (authenticated)
- `DELETE /api/books/<id>/` — Delete a book (authenticated)

### Permissions
- Unauthenticated users: Can only read data.
- Authenticated users: Can create, update, and delete books.


"""
Filtering:
- /api/books/?title=AI
- /api/books/?publication_year=2023
- /api/books/?author=1

Search:
- /api/books/?search=deep learning

Ordering:
- /api/books/?ordering=title
- /api/books/?ordering=-publication_year
"""

✅ 1. Basic GET Request – List All Books
bash
Copier le code
curl -X GET http://127.0.0.1:8000/api/books/
✅ 2. Filtering by Title
bash
Copier le code
curl -X GET "http://127.0.0.1:8000/api/books/?title=AI"
✅ 3. Filtering by Author ID and Publication Year
bash
Copier le code
curl -X GET "http://127.0.0.1:8000/api/books/?author=2&publication_year=2024"
✅ 4. Search by Title or Author Name
(assuming search_fields = ['title', 'author__name'])

bash
Copier le code
curl -X GET "http://127.0.0.1:8000/api/books/?search=achraf"
✅ 5. Ordering by Title (A-Z)
bash
Copier le code
curl -X GET "http://127.0.0.1:8000/api/books/?ordering=title"
✅ 6. Ordering by Publication Year (Newest First)
bash
Copier le code
curl -X GET "http://127.0.0.1:8000/api/books/?ordering=-publication_year"