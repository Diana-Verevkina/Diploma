from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author
from django.core.paginator import Paginator


def index(request):
    template = 'index.html'
    return render(request, template)


def books(request):
    template = 'books.html'
    books_objects = Book.objects.order_by('-year')
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Books',
        'books': books_objects,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def book_detail(request, id):
    template = 'book_detail.html'
    books_objects = get_object_or_404(Book, id=id)
    context = {
        'book': books_objects
    }
    return render(request, template, context)


def author_detail(request, id):
    template = 'author_detail.html'
    author = get_object_or_404(Author, id=id)
    book_list = author.books.distinct()
    context = {
        'author': author,
        'book_list': book_list,
    }
    return render(request, template, context)


def authors(request):
    template = 'authors.html'
    author_objects = Author.objects.all()
    author_list = Author.objects.all()
    paginator = Paginator(author_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Authors',
        'authors': author_objects,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def recommendations(request):
    template = 'recommendations.html'
    context = {
        'title': 'Recommendations',
    }
    return render(request, template, context)
