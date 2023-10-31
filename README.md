# Image-Upload-API
A recruitment task done in Django REST Framework. It enables user to upload and list their pictures.

## API Endpoints
```images/create/``` - user can upload images via an HTTP POST request.

```images/list/``` - user can list their uploaded images via an HTTP GET request.

```delete_images/<int:pk>/``` - user can delete a specific image based on their PK.

```expiring-links/``` - user can create an expiring link to his image with a given expiration time (not fully working for now - expiring link doesn't lead to the picture)

## Account Tiers
- Basic: users receive a link to a 200px thumbnail.
- Premium: users receive links to a 200px thumbnail, a 400px thumbnail, and the original image.
- Enterprise: users receive links to a 200px thumbnail, a 400px thumbnail, and the original image, with the ability to specify the link expiration time.

## Admin Panel
Admins can create and configure arbitrary tiers with customizable settings.

Use the Django admin interface (/admin) to manage account tiers and users.

## Setup
To launch the project launch a virtual environment, then run:

```pip install -r requirements.txt```

then create and apply migrations:

```python manage.py makemigrations```

```python manage.py migrate```

then create a superuser to have access to admin panel:

```python manage.py createsuperuser``` - pass your desired username and password

to setup built-in tiers run:

```python manage.py setup_tiers```

lastly, to run the server execute:

```python manage.py runserver```