from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from .forms import BookForm, AuthorForm, CommentForm
from .models import Book, Author, Comment
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
    if request.user.is_authenticated and request.user.username == 'diana':
        may_delete = True
    else:
        may_delete = False
    form = CommentForm(request.POST or None)
    context = {
        'book': books_objects,
        'may_delete': may_delete,
        'form': form,
        'comments': books_objects.comments.all(),
    }
    return render(request, template, context)


def book_create(request):
    form = BookForm(request.POST or None, files=request.FILES or None, )
    if not form.is_valid():
        return render(request, 'create_book.html', {'form': form})
    book = form.save(commit=False)
    book.save()
    return redirect('books:books')


def book_edit(request, id):
    book = get_object_or_404(Book, id=id)

    form = BookForm(request.POST or None, files=request.FILES or None,
                    instance=book)
    if form.is_valid():
        form.save()
        return redirect('books:book_detail', id)
    return render(request, 'create_book.html', {'form': form})


def author_edit(request, id):
    author = get_object_or_404(Author, id=id)

    form = AuthorForm(request.POST or None, files=request.FILES or None,
                      instance=author)
    if form.is_valid():
        form.save()
        return redirect('books:author_detail', id)
    return render(request, 'create_author.html', {'form': form})


def author_detail(request, id):
    template = 'author_detail.html'
    author = get_object_or_404(Author, id=id)
    book_list = author.books.distinct()
    if request.user.is_authenticated and request.user.username == 'diana':
        may_delete = True
    else:
        may_delete = False
    context = {
        'author': author,
        'book_list': book_list,
        'may_delete': may_delete
    }
    return render(request, template, context)


def author_create(request):
    form = AuthorForm(request.POST or None, files=request.FILES or None, )
    if not form.is_valid():
        return render(request, 'create_author.html', {'form': form})
    author = form.save(commit=False)
    author.save()
    return redirect('books:authors')


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


def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books:books')


def author_delete(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    return redirect('books:authors')


def recommendations(request):
    template = 'recommendations.html'
    context = {
        'title': 'Recommendations',
    }
    return render(request, template, context)


def add_comment(request, id):
    book = get_object_or_404(Book, id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.book = book
        comment.save()
    return redirect('books:book_detail', id=id)


def delete_comment(request, id, comment_id):
    Comment.objects.filter(id=comment_id).delete()
    return redirect('books:book_detail', id=id)


def object_not_found(request):
    template = 'object_not_found.html'
    return render(request, template)


def search_book(request):
    query = request.GET.get('q')
    try:
        object_list = Book.objects.filter(name__icontains=query)
        return redirect('books:book_detail', id=object_list.first().id)
    except:
        return redirect('books:object_not_found')



def search_author(request):
    query = request.GET.get('q')
    try:
        object_list = Author.objects.filter(author_name__icontains=query)
        return redirect('books:author_detail', id=object_list.first().id)
    except:
        return redirect('books:object_not_found')
