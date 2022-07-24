from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'section', 'description')
    list_filter = ('author',)
    #empty_value_display = '-пусто-'
    list_per_page = 10


admin.site.register(Book, BookAdmin)


