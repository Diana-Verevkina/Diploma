from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books', views.books),
    path('/authors/<int:id>/', views.author_detail, name='author_detail'),
    path('authors/', views.authors),
    path('recommendations', views.recommendations),
    # path('detail', views.book_details)
]
