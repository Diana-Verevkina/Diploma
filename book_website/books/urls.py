from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('authors', views.authors),
    path('recommendations', views.recommendations),
    # path('detail', views.book_details)
    path('books/<int:index>/', views.book_detail, name='book_detail')
]
