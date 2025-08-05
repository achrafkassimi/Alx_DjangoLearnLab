- (venv) C:\Users\melua\Documents\Alx_DjangoLearnLab\advanced-api-project>python manage.py createsuperuser
Username (leave blank to use 'achraf'): achraf
Email address: achraf@gmail.com
Password: 1234
Password (again): 1234


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
