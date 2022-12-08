from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Author(models.Model):
    # имя автора
    author_name = models.CharField(max_length=50)
    # имя автора маленькими буквами
    author_name_lower = models.CharField(max_length=200, blank=True, null=True)
    # url фото автора (загружаем с базой данных)
    author_photo = models.TextField(blank=True, null=True)
    # фото автора, добавляемое пользователем через форму на сайте
    photo = models.ImageField('Картинка', upload_to='authors/', blank=True,
                              null=True)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    name = models.CharField(max_length=200)
    # название книги маленькими буквами
    name_lower = models.CharField(max_length=200, blank=True, null=True)
    # имя автора текстом (после парсера)
    author = models.CharField(max_length=50, blank=True, null=True)
    # раздел литературы
    section = models.CharField(max_length=50)
    # издательство
    publish = models.CharField(max_length=50, default=None,
                               blank=True, null=True)
    # ограничение по возрасту
    age = models.CharField(max_length=5)
    # год выпуска
    year = models.CharField(max_length=5)
    # количество страниц
    pages = models.CharField(max_length=10, blank=True, null=True)
    rating = models.CharField(max_length=10, blank=True, null=True)
    # ссылка на фото обложки книги
    cove = models.TextField(blank=True, null=True)
    # описание книги
    description = models.TextField()
    author_id = models.ForeignKey(Author, verbose_name='Автор',
                                  on_delete=models.SET_NULL, blank=True,
                                  null=True, related_name='books')
    # фото обложки книги, добавляемое пользователем через форму на сайте
    image = models.ImageField('Картинка', upload_to='books/', blank=True)
    # тэги книги - описания, обработанные spacy в начальной форме,
    # без стоп-слов, без окончаний
    tags = models.TextField(blank=True, null=True)
    # вектор, созданный из tags
    vector = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


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
