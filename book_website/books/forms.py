from django import forms

from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'section', 'publish', 'age', 'year',
                  'pages', 'description', 'author_id', 'image')
        """labels = {'text': 'Введите текст', 'group': 'Выберите группу'}
        help_texts = {'text': 'Здесь напишите свой пост',
                      'group': 'Выберите группу из существующих',
                      'image': 'Выберите изображение'}"""


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('author_name', 'photo')
