from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_photo = models.TextField()

    def __str__(self):
        return self.author_name


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    publish = models.CharField(max_length=50, default=None)
    age = models.CharField(max_length=5)
    year = models.CharField(max_length=5)
    pages = models.IntegerField()
    rating = models.FloatField(blank=True, null=True)
    cove = models.TextField()
    description = models.TextField()
    author_photo = models.TextField(blank=True, null=True)
    author_id = models.ForeignKey(Author, verbose_name='Автор',
                                  on_delete=models.SET_NULL, blank=True,
                                  null=True, related_name='books')

    def __str__(self):
        return str(self.id)

