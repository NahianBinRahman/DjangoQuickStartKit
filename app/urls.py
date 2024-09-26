# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL to the home view
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # Define 'some_view' if you are using it
    path('some-url/', views.some_view, name='some_view'),
]
