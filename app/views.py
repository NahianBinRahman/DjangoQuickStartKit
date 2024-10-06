# myapp/views.py
from django.shortcuts import render
from .models import Member


def home(request):
    return render(request, 'home.html')


def about(request):
    members = Member.objects.all()  # Fetch all members from the database
    return render(request, 'about.html', {'members': members})


def contact(request):
    return render(request, 'contact.html')


def some_view(request):
    # This view should return a partial template or content
    if request.htmx:
        return render(request, 'partials/some_partial.html')
    return render(request, 'home.html')
