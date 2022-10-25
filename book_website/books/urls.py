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
    path('books/<int:id>/edit/', views.book_edit, name='book_edit'),
    path('/authors/<int:id>/edit/', views.author_edit, name='author_edit'),
    path('author_create/', views.author_create, name='author_create'),
    path('books/<int:id>/delete', views.book_delete, name='book_delete'),
    path('books/<int:id>/comment/', views.add_comment,
         name='add_comment'),
    path('books/<int:id>/comment/<int:comment_id>/delete', views.delete_comment,
         name='delete_comment'),
    path('/authors/<int:id>/delete', views.author_delete, name='author_delete'),

    path('search_book/', views.search_book, name='search_book'),
    path('search_author/', views.search_author, name='search_author'),

    path('object_not_found/', views.object_not_found, name='object_not_found'),
    path('favorites/', views.favorites, name='favorites'),
    path('make_favore/<int:id>/', views.make_favore, name='make_favore'),
    path('make_not_favore/<int:id>/', views.make_not_favore, name='make_not_favore'),

]
