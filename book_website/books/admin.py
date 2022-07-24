from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('index', 'name', 'author', 'section', 'description')
    list_filter = ('name', 'author')
    #empty_value_display = '-пусто-'


admin.site.register(Book, BookAdmin)


