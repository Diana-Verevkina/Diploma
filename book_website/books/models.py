from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_photo = models.TextField(blank=True, null=True)
    photo = models.ImageField('Картинка', upload_to='authors/', blank=True)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50, blank=True, null=True)
    section = models.CharField(max_length=50)
    publish = models.CharField(max_length=50, default=None)
    age = models.CharField(max_length=5)
    year = models.CharField(max_length=5)
    pages = models.IntegerField()
    rating = models.FloatField(blank=True, null=True)
    cove = models.TextField(blank=True, null=True)
    description = models.TextField()
    author_photo = models.TextField(blank=True, null=True)
    author_id = models.ForeignKey(Author, verbose_name='Автор',
                                  on_delete=models.SET_NULL, blank=True,
                                  null=True, related_name='books')
    image = models.ImageField('Картинка', upload_to='books/', blank=True)
    is_favore = models.BooleanField(default=False, blank=True, null=True)
    #favorites = models.ManyToManyField(User, through='FavoreBook')

    def __str__(self):
        return str(self.id)


class FavoreBook(models.Model):
    person = models.ForeignKey(
        User, verbose_name='Пользователь, который поставил like',
        on_delete=models.CASCADE, blank=True,
        null=True, related_name='FavoreBook',
        help_text='Ссылка пользователя, который поставил like')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorite_books')


class Comment(models.Model):
    book = models.ForeignKey(Book, verbose_name='Книга',
                             on_delete=models.CASCADE, blank=True,
                             null=True, related_name='comments',
                             help_text='Ссылка на книгу, к которой оставлен '
                                       'комментарий')
    author = models.ForeignKey(User, verbose_name='Автор',
                               on_delete=models.CASCADE, blank=True,
                               null=True, related_name='comments',
                               help_text='Ссылка на автора комментария')
    text = models.TextField(verbose_name='Текст комментария',
                            help_text='Введите текст комментария')
    created = models.DateTimeField(verbose_name='Дата публикации комментария',
                                   auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:15]
