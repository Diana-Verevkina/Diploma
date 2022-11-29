from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BookForm, AuthorForm, CommentForm
from .models import Book, Author, Comment, FavoreBook
from .recommendations import recommend


def index(request):
    template = 'index.html'
    return render(request, template)


def books(request):
    template = 'books.html'
    books_objects = Book.objects.order_by('-year')
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 64)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    favore_flags = []
    if request.user.is_authenticated:
        favore_books = FavoreBook.objects.filter(person=request.user)
        for favorite in favore_books:
            favore_flags.append(favorite.book.id)
    else:
        favore_books = []

    context = {
        'title': 'Books',
        'books': books_objects,
        'page_obj': page_obj,
        'favore_books': favore_books,
        'favore_flags': favore_flags
    }
    return render(request, template, context)


@login_required
def recommendations(request):
    template = 'recommendations.html'

    recommend_books = recommend('Психолог в концлагере ')
    context = {
        'title': 'Recommendations',
        'recommend_books': recommend_books
    }
    return render(request, template, context)


def search_book_recommend(request):
    query = request.GET.get('q')
    try:
        for_recommend = Book.objects.filter(name__icontains=query)
        for_recommend_name = for_recommend[0].name
        books_rec_list = []
        recommend_books = recommend(for_recommend_name)
        for book_name in recommend_books:
            if Book.objects.filter(name__icontains=book_name.strip()):
                books_rec_list.append(Book.objects.filter(name__icontains=book_name.strip()))
        test = books_rec_list[0]
        for book in books_rec_list[1:]:
            test = test | book

        paginator = Paginator(test, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'title': 'Books',
            'books': test,
            'page_obj': page_obj,
            'book_name': for_recommend_name
        }
        return render(request, 'recommendations.html', context)
    except:
        return redirect('books:object_not_found')


def book_recommend(request, id):
    try:
        for_recommend = Book.objects.filter(id=id)
        for_recommend_name = for_recommend[0].name
        books_rec_list = []
        recommend_books = recommend(for_recommend_name)
        for book_name in recommend_books:
            if Book.objects.filter(name__icontains=book_name.strip()):
                books_rec_list.append(Book.objects.filter(name__icontains=book_name.strip()))
        test = books_rec_list[0]
        for book in books_rec_list[1:]:
            test = test | book

        paginator = Paginator(test, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'title': 'Books',
            'books': test,
            'page_obj': page_obj,
            'book_name': for_recommend_name
        }
        return render(request, 'recommendations.html', context)
    except:
        return redirect('books:object_not_found')


@login_required
def make_favore(request, id):
    template = 'make_favore.html'
    favorite_book = get_object_or_404(Book, id=id)
    FavoreBook.objects.get_or_create(person=request.user, book=get_object_or_404(Book, id=id))
    context = {
        'book': favorite_book,
    }
    return render(request, template, context)


@login_required
def make_not_favore(request, id):
    template = 'make_not_favore.html'
    not_favore = get_object_or_404(Book, id=id)
    FavoreBook.objects.filter(person=request.user, book=get_object_or_404(Book, id=id)).delete()
    context = {
        'book': not_favore,
    }
    return render(request, template, context)


@login_required
def favorites(request):
    template = 'favorites.html'
    books_objects = FavoreBook.objects.filter(person=request.user)
    paginator = Paginator(books_objects, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
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
    favore_flags = []
    if request.user.is_authenticated:
        favore_books = FavoreBook.objects.filter(person=request.user)
        for favorite in favore_books:
            favore_flags.append(favorite.book.id)
    context = {
        'book': books_objects,
        'may_delete': may_delete,
        'form': form,
        'comments': books_objects.comments.all(),
        'favore_flags': favore_flags
    }
    return render(request, template, context)


@login_required
def book_create(request):
    form = BookForm(request.POST or None, files=request.FILES or None, )
    if not form.is_valid():
        return render(request, 'create_book.html', {'form': form})
    book = form.save(commit=False)
    book.save()
    return redirect('books:books')


@login_required
def book_edit(request, id):
    book = get_object_or_404(Book, id=id)

    form = BookForm(request.POST or None, files=request.FILES or None,
                    instance=book)
    if form.is_valid():
        form.save()
        return redirect('books:book_detail', id)
    return render(request, 'create_book.html', {'form': form})


@login_required
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


@login_required
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
    paginator = Paginator(author_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Authors',
        'authors': author_objects,
        'page_obj': page_obj,
    }
    return render(request, template, context)


@login_required
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books:books')


@login_required
def author_delete(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    return redirect('books:authors')


@login_required
def add_comment(request, id):
    book = get_object_or_404(Book, id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.book = book
        comment.save()
    return redirect('books:book_detail', id=id)


@login_required
def delete_comment(request, id, comment_id):
    Comment.objects.filter(id=comment_id).delete()
    return redirect('books:book_detail', id=id)


def object_not_found(request):
    template = 'object_not_found.html'
    return render(request, template)


def search_book(request):
    query = request.GET.get('q')
    try:
        object_list = Book.objects.filter(name_lower__icontains=query.lower())
        if len(object_list) < 1:
            return redirect('books:object_not_found')
        paginator = Paginator(object_list, 64)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'title': 'Books',
            'books': object_list,
            'page_obj': page_obj
        }
        return render(request, 'books.html', context)
    except:
        return redirect('books:object_not_found')


def search_author(request):
    query = request.GET.get('q')
    try:
        object_list = Author.objects.filter(author_name_lower__icontains=query.lower())
        paginator = Paginator(object_list, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'title': 'Authors',
            'authors': object_list,
            'page_obj': page_obj,
        }
        return render(request, 'authors.html', context)
        # return redirect('books:author_detail', id=object_list.first().id)
    except:
        return redirect('books:object_not_found')


def search_favorite_book(request):
    query = request.GET.get('q')
    try:
        books_objects = FavoreBook.objects.filter(person=request.user,
                                                  book__name_lower__icontains
                                                  =query.lower())
        if len(books_objects) < 1:
            return redirect('books:object_not_found')
        paginator = Paginator(books_objects, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'books': books_objects,
            'page_obj': page_obj,
        }
        return render(request, 'favorites.html', context)
    except:
        return redirect('books:object_not_found')
