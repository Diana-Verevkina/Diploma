from django import forms

from .models import Book, Author, Comment, Section


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('name',)
        labels = {'name': 'Название секции'}


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        section = forms.ModelChoiceField(queryset=Section.objects.all(),
                                       required=False)
        fields = ('name', 'section_id', 'publish', 'age', 'year',
                  'pages', 'description', 'author_id', 'image')


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
