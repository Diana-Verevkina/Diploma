from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    template = 'index.html'
    return render(request, template)


def books(request):
    template = 'books.html'
    books_objects = Book.objects.order_by('-year')
    context = {
        'title': 'Books',
        'books': books_objects
    }
    return render(request, template, context)


def authors(request):
    template = 'authors.html'
    context = {
        'title': 'Authors',
    }
    return render(request, template, context)

def recommendations(request):
    template = 'recommendations.html'
    context = {
        'title': 'Recommendations',
    }
    return render(request, template, context)