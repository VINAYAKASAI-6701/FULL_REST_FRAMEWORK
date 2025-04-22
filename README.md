FULL REST FRAMEWORK
This project demonstrates how to create and expose APIs using Django Rest Framework (DRF). It includes basic CRUD operations for a Book model with a simple API to manage the records.

Table of Contents
Installation

Setup

Creating Superuser

Running the Project

API Endpoints

GET Request

POST Request

PUT Request

DELETE Request

Testing the API in Postman

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/VINAYAKASAI-6701/FULL_REST_FRAMEWORK.git
Navigate to the project directory:

bash
Copy
Edit
cd FULL_REST_FRAMEWORK
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

Windows:

bash
Copy
Edit
venv\Scripts\activate
Mac/Linux:

bash
Copy
Edit
source venv/bin/activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt does not exist, install Django and DRF manually:

bash
Copy
Edit
pip install django djangorestframework
Setup
Create a Django Project: If not already created, initialize the Django project:

bash
Copy
Edit
django-admin startproject drfproj
Create the Application:

bash
Copy
Edit
python manage.py startapp drfapp
Configure Installed Apps: Add 'rest_framework' and 'drfapp' to the INSTALLED_APPS list in drfproj/settings.py.

python
Copy
Edit
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drfapp',
]
Define Models: Create a simple Book model in drfapp/models.py:

python
Copy
Edit
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
Create Serializers: Create a serializer to convert the model data to JSON in drfapp/serializers.py:

python
Copy
Edit
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
Create Views: In drfapp/views.py, create a view to handle API requests:

python
Copy
Edit
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
Set Up URLs: Include the API URLs in drfproj/urls.py:

python
Copy
Edit
from rest_framework.routers import DefaultRouter
from drfapp.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
Migrate the Database: Apply migrations to create the database tables:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Creating Superuser
Create a superuser to access the Django Admin Panel:

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to create the superuser account.

Running the Project
Start the development server:

bash
Copy
Edit
python manage.py runserver
The project will be accessible at:
http://127.0.0.1:8000/

API Endpoints
GET Request
URL: http://127.0.0.1:8000/api/books/

Method: GET

Description: Retrieves a list of all books in the system.

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "title": "Book Title",
    "author": "Author Name",
    "published_date": "2025-01-01"
  }
]
POST Request
URL: http://127.0.0.1:8000/api/books/

Method: POST

Body:

json
Copy
Edit
{
  "title": "Django for Beginners",
  "author": "John Doe",
  "published_date": "2025-01-01"
}
Description: Adds a new book to the system.

Response:

json
Copy
Edit
{
  "id": 1,
  "title": "Django for Beginners",
  "author": "John Doe",
  "published_date": "2025-01-01"
}
PUT Request
URL: http://127.0.0.1:8000/api/books/{id}/

Method: PUT

Body:

json
Copy
Edit
{
  "title": "Updated Django for Beginners",
  "author": "John Doe",
  "published_date": "2025-02-01"
}
Description: Updates a specific book record.

Response:

json
Copy
Edit
{
  "id": 1,
  "title": "Updated Django for Beginners",
  "author": "John Doe",
  "published_date": "2025-02-01"
}
DELETE Request
URL: http://127.0.0.1:8000/api/books/{id}/

Method: DELETE

Description: Deletes a specific book record.

Response: Empty body with status code 204 No Content.

Testing the API in Postman
GET Request:

URL: http://127.0.0.1:8000/api/books/

Method: GET

Expected Response: List of books in JSON format.

POST Request:

URL: http://127.0.0.1:8000/api/books/

Method: POST

Body: Raw JSON

json
Copy
Edit
{
  "title": "Django for Beginners",
  "author": "John Doe",
  "published_date": "2025-01-01"
}
Expected Response: JSON of the newly created book.

PUT Request:

URL: http://127.0.0.1:8000/api/books/{id}/

Method: PUT

Body: Raw JSON

json
Copy
Edit
{
  "title": "Updated Django for Beginners",
  "author": "John Doe",
  "published_date": "2025-02-01"
}
Replace {id} with the actual book ID.

Expected Response: JSON of the updated book.

DELETE Request:

URL: http://127.0.0.1:8000/api/books/{id}/

Method: DELETE

Expected Response: Empty body with status code 204.

