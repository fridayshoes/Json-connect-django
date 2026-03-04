"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import the admin module to provide the path for the Django admin site
from django.contrib import admin

# 'path' defines individual routes; 'include' allows you to reference other urls.py files
from django.urls import path, include

urlpatterns = [
    # Route for the admin dashboard. 
    # Usually accessible at http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    # This is a "Redirector" for your app.
    # It tells Django: "If the URL starts with 'service1/', 
    # stop looking here and go look inside 'service1/urls.py' for the rest."
    path('service1/', include('service1.urls')),
]
