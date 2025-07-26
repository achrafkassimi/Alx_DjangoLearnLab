# Alx_DjangoLearnLab
Welcome to the “Introduction to Django” project. This project is tailored for you to help you gain hands-on experience with Django, one of the most popular web frameworks for building robust web applications. 



## in CMD (Command) or Powershell run this code, it works fine:

validation
- python manage.py runserver
- python -m django --help
start a new project
- python -m django startproject mysite


Visit the following URLs in your browser:

http://localhost:8000/relationship/books/: Displays a list of all books.

http://localhost:8000/relationship/library/1/: Displays details for the library with ID 1 (make sure you have a library with ID 1).


Visit the following URLs:

- Register: http://localhost:8000/relationship/register/

- Login: http://localhost:8000/relationship/login/

- Logout: http://localhost:8000/relationship/logout/

You should be able to:

- Register a new user.
- Log in using the credentials.
- Log out from the application.


# Permissions and Groups Setup

We use Django's built-in permissions and groups system to control access:

## Custom Permissions (Book model):
- can_view
- can_create
- can_edit
- can_delete

## Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

## Usage:
Permissions are checked in views using the @permission_required decorator.

To assign a user to a group:
1. Go to Django admin
2. Select a user → choose group

To create groups with permissions via shell, run:
python manage.py shell


# Security Review - HTTPS Implementation

## Implemented Settings

- `SECURE_SSL_REDIRECT = True`: Forces all HTTP traffic to redirect to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enforces strict HTTPS access for 1 year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS policy to all subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows site to be preloaded in browsers’ HSTS lists.
- `SESSION_COOKIE_SECURE = True` and `CSRF_COOKIE_SECURE = True`: Ensures cookies only sent over HTTPS.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking attacks.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS protection.

## Deployment

- SSL is configured using Let’s Encrypt in the Nginx reverse proxy setup.
- HTTP traffic is automatically redirected to HTTPS.

## Notes

- All security settings are disabled when `DEBUG=True`, so production must always use `DEBUG=False`.
- Regular audits recommended.
