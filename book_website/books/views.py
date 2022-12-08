import re

import nltk
import pandas as pd
import spacy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer

from .forms import BookForm, AuthorForm, CommentForm
from .models import Book, Author, Comment, FavoreBook
from .recommendations import recommend


def index(request):
    """Главная страница."""

    template = 'index.html'
    return render(request, template)


def get_favore_flags(request):
    """Отображение избранных книг."""

    favore_flags = []
    if request.user.is_authenticated:
        # все избранные книги для данного пользователя
        favore_books = FavoreBook.objects.filter(person=request.user)
        # если книга в избранном, добавляем ее id в список
        for favorite in favore_books:
            favore_flags.append(favorite.book.id)
    else:
        # для неавторизованных пользователей избранные книги недоступны
        favore_books = []
    return favore_books, favore_flags


def books(request):
    """Страница со списком книг."""

    template = 'books/books.html'
    books_objects = Book.objects.order_by('-year')
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 64)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    favore_books, favore_flags = get_favore_flags(request)

    context = {
        'title': 'Books',
        'books': books_objects,
        'page_obj': page_obj,
        'favore_books': favore_books,
        'favore_flags': favore_flags
    }
    return render(request, template, context)


def book_detail(request, id):
    """Детали о книге."""
    template = 'books/book_detail.html'
    books_objects = get_object_or_404(Book, id=id)
    if request.user.is_authenticated and request.user.username == 'diana':
        may_delete = True
    else:
        may_delete = False
    form = CommentForm(request.POST or None)
    favore_books, favore_flags = get_favore_flags(request)

    context = {
        'book': books_objects,
        'may_delete': may_delete,
        'form': form,
        'comments': books_objects.comments.all(),
        'favore_flags': favore_flags
    }
    return render(request, template, context)


@login_required
def recommendations(request):
    """Страница рекомендаций."""

    template = 'recommendations.html'
    context = {
        'title': 'Recommendations',
    }
    return render(request, template, context)


def book_recommend(request, id, for_recommend=False):
    """Вывод рекомендаций к выбранной книге."""

    try:
        if not for_recommend:
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
    """Добавить книгу в избранное."""

    template = 'books/make_favore.html'
    favorite_book = get_object_or_404(Book, id=id)
    FavoreBook.objects.get_or_create(person=request.user,
                                     book=get_object_or_404(Book, id=id))
    context = {
        'book': favorite_book,
    }
    return render(request, template, context)


@login_required
def make_not_favore(request, id):
    """Удалить книгу из избранного."""

    template = 'books/make_not_favore.html'
    not_favore = get_object_or_404(Book, id=id)
    FavoreBook.objects.filter(person=request.user,
                              book=get_object_or_404(Book, id=id)).delete()
    context = {
        'book': not_favore,
    }
    return render(request, template, context)


@login_required
def favorites(request):
    """Избранное."""

    template = 'books/favorites.html'
    books_objects = FavoreBook.objects.filter(person=request.user)
    paginator = Paginator(books_objects, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'books': books_objects,
        'page_obj': page_obj,
    }
    return render(request, template, context)


# region add_tags
def stopslova(text):
    """Удаляет стоп-слова и возвращает текст без них."""

    y = []
    stop_words = stopwords.words('russian')
    for i in text.split():
        if not i in stop_words:
            y.append(i)
    return " ".join(y)


def spacylem(text):
    """Обработка текста через spacy."""

    nlp = spacy.load('ru_core_news_sm')
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc]
    return " ".join(tokens)


def stemming(text):
    """Стемминг - отрезание окончаний слов."""

    stemmer = SnowballStemmer(language='russian')
    tokenizer = nltk.tokenize.WhitespaceTokenizer()
    tokens = [stemmer.stem(w) for w in tokenizer.tokenize(text)]
    return " ".join(tokens)


def tags_create(description, section):
    """Создание тегов из описаний книг."""
    description = re.sub("[^А-Яа-я, ё, \n, -]", "", description)
    description = description.lower()
    description = re.sub(",", " ", description)
    description = re.sub("\n", " ", description)
    description = re.sub("-", " ", description)
    description_without_stopwords = stopslova(description)
    description_spacy = spacylem(description_without_stopwords)
    description_stemming = stemming(description_spacy)
    return description_stemming + section
# endregion


def vector_add(name, tag):
    """Добавление вектора по тегам в базу при добавлении новой книги."""

    cv = CountVectorizer(encoding='utf-8')
    data = pd.read_csv('/Users/dianaverevkina/Diplom_project/'
                       'Diploma — копия 3/data_preparation/spacylem.csv')
    data.loc[len(data.index)] = [name, tag]
    data.to_csv(r'/Users/dianaverevkina/Diplom_project/Diploma — копия 3/'
                r'data_preparation/spacylem.csv', index=False)

    cv.fit(data['tags'])
    vectors = cv.fit_transform(data['tags'].values.astype('U'))
    vector = vectors[-1]
    return vector


@login_required
def book_create(request):
    """Добавление новой книги."""

    form = BookForm(request.POST or None, files=request.FILES or None, )
    if not form.is_valid():
        return render(request, 'books/create_book.html', {'form': form})
    book = form.save(commit=False)
    book.tags = tags_create(book.description, book.section)
    book.vector = vector_add(book.name, book.tags)
    book.name_lower = book.name.lower()
    book.save()
    return redirect('books:books')


@login_required
def book_edit(request, id):
    """Редактирование книги."""

    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, files=request.FILES or None,
                    instance=book)
    if form.is_valid():
        form.save()
        return redirect('books:book_detail', id)
    return render(request, 'books/create_book.html', {'form': form})


@login_required
def author_edit(request, id):
    """Редактирование автора."""

    author = get_object_or_404(Author, id=id)
    form = AuthorForm(request.POST or None, files=request.FILES or None,
                      instance=author)
    if form.is_valid():
        form.save()
        return redirect('books:author_detail', id)
    return render(request, 'authors/create_author.html', {'form': form})


def author_detail(request, id):
    """Детали об авторе."""

    template = 'authors/author_detail.html'
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
    """Добавление нового автора."""

    form = AuthorForm(request.POST or None, files=request.FILES or None, )
    if not form.is_valid():
        return render(request, 'authors/create_author.html', {'form': form})
    author = form.save(commit=False)
    author.save()
    return redirect('books:authors')


def authors(request):
    """Отображение списка авторов."""

    template = 'authors/authors.html'
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
    """Удаление книги."""

    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books:books')


@login_required
def author_delete(request, id):
    """Удаление автора."""

    author = get_object_or_404(Author, id=id)
    author.delete()
    return redirect('books:authors')


@login_required
def add_comment(request, id):
    """Добавление коментария."""

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
    """Удаление коментария."""

    Comment.objects.filter(id=comment_id).delete()
    return redirect('books:book_detail', id=id)


def object_not_found(request):
    """Функция отображения страницы object_not_found.html"""

    template = 'object_not_found.html'
    return render(request, template)


def search_book(request):
    """Поиск книги по названию."""

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
        return render(request, 'books/books.html', context)
    except:
        return redirect('books:object_not_found')


def search_author(request):
    """Поиск автора по имени."""

    query = request.GET.get('q')
    try:
        object_list = Author.objects.filter(
            author_name_lower__icontains=query.lower()
        )
        paginator = Paginator(object_list, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'title': 'Authors',
            'authors': object_list,
            'page_obj': page_obj,
        }
        return render(request, 'authors/authors.html', context)
    except:
        return redirect('books:object_not_found')


def search_favorite_book(request):
    """Поиск избранной книги по названию."""

    query = request.GET.get('q')
    try:
        books_objects = FavoreBook.objects.filter(
            person=request.user, book__name_lower__icontains=query.lower()
        )
        if len(books_objects) < 1:
            return redirect('books:object_not_found')
        paginator = Paginator(books_objects, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'books': books_objects,
            'page_obj': page_obj,
        }
        return render(request, 'books/favorites.html', context)
    except:
        return redirect('books:object_not_found')
