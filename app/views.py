# myapp/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def some_view(request):
    # This view should return a partial template or content
    if request.htmx:
        return render(request, 'partials/some_partial.html')
    return render(request, 'home.html')
