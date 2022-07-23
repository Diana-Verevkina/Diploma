from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('authors', views.authors),
    path('recommendations', views.recommendations),
    path('detail', views.book_details)
]
