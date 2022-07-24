from django.shortcuts import render, get_object_or_404
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


def book_detail(request, id):
    template = 'book_detail.html'
    books_objects = get_object_or_404(Book, id=id)
    context = {
        'book': books_objects
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
