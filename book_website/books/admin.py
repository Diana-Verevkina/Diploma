from django.contrib import admin
from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'section', 'description')
    list_filter = ('author',)
    #empty_value_display = '-пусто-'
    list_per_page = 10


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)

