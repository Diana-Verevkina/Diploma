from django.db import models


class Book(models.Model):
    index = models.IntegerField(default=None, primary_key=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    publish = models.CharField(max_length=50, default=None)
    age = models.CharField(max_length=5)
    year = models.CharField(max_length=5)
    pages = models.IntegerField()
    rating = models.FloatField()
    cove = models.TextField()
    description = models.TextField()

    def __str__(self):
        return str(self.index)
