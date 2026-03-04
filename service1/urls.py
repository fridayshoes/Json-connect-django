# Import the admin module to allow access to the Django admin interface
from django.contrib import admin

# Import the path function which is used to define URL patterns
from django.urls import path

# Import the views file from the current directory (.) to link URLs to logic
from . import views

# A list of URL patterns that Django matches against incoming browser requests
urlpatterns = [
    # Route for the built-in Django admin panel (usually http://127.0.0.1:8000/admin/)
    path('admin/', admin.site.urls),
    
    # The 'Root' route (empty string '') - this is your homepage.
    # It tells Django to run the 'read_json' function located in views.py.
    # The 'name' parameter allows you to refer to this URL in your HTML templates.
    path('', views.read_json, name='read_json'),
]