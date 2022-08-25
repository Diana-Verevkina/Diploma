from django import forms

from .models import Book, Author, Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'section', 'publish', 'age', 'year',
                  'pages', 'description', 'author_id', 'image')
        """labels = {'text': 'Введите текст', 'group': 'Выберите группу'}
        help_texts = {'text': 'Здесь напишите свой пост',
                      'group': 'Выберите группу из существующих',
                      'image': 'Выберите изображение'}"""


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('author_name', 'photo')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': 'Текст комментария'}
        help_texts = {'text': 'Введите текст комментария'}
