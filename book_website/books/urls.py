from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),

    # детали книги - book_detail
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    # книги - books
    path('books', views.books, name='books'),
    # редактирование книги - book_edit
    path('books/<int:id>/edit/', views.book_edit, name='book_edit'),
    # удаление книги - book_delete
    path('books/<int:id>/delete', views.book_delete, name='book_delete'),
    # создание книги - book_create
    path('book_create/', views.book_create, name='book_create'),
    # поиск книги - search_book
    path('search_book/', views.search_book, name='search_book'),
    # поиск избранной книги - search_favorite_book
    path('search_favorite_book/', views.search_favorite_book,
         name='search_favorite_book'),
    # рекомендации для книги - book_recommend
    path('book_recommend/<int:id>', views.book_recommend,
         name='book_recommend'),
    # рекомендации - recommendations
    path('recommendations', views.recommendations, name='recommendations'),

    # избранные книги - favorites
    path('favorites/', views.favorites, name='favorites'),
    # добавление книги в избранное - make_favore
    path('make_favore/<int:id>/', views.make_favore, name='make_favore'),
    # удаление книги из избранное - make_not_favore
    path('make_not_favore/<int:id>/', views.make_not_favore,
         name='make_not_favore'),

    # добавление комментария - add_comment
    path('books/<int:id>/comment/', views.add_comment, name='add_comment'),
    # удаление комментария - delete_comment
    path('books/<int:id>/comment/<int:comment_id>/delete',
         views.delete_comment, name='delete_comment'),

    # автор - author_detail
    path('/authors/<int:id>/', views.author_detail, name='author_detail'),
    # авторы - authors
    path('authors/', views.authors, name='authors'),
    # редактирование автора - author_edit
    path('/authors/<int:id>/edit/', views.author_edit, name='author_edit'),
    # добавление автора - author_create
    path('author_create/', views.author_create, name='author_create'),
    # удаление автора - author_delete
    path('/authors/<int:id>/delete', views.author_delete, name='author_delete'),
    # поиск автора - search_author
    path('search_author/', views.search_author, name='search_author'),

    # объект не найден - object_not_found
    path('object_not_found/', views.object_not_found, name='object_not_found'),

    path('section_create/', views.section_create, name='section_create'),
]
