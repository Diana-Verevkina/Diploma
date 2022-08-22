from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books', views.books, name='books'),
    path('/authors/<int:id>/', views.author_detail, name='author_detail'),
    path('authors/', views.authors, name='authors'),
    path('recommendations', views.recommendations),
    path('book_create/', views.book_create, name='book_create'),
    path('author_create/', views.author_create, name='author_create'),
]
