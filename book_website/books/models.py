from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    age = models.CharField(max_length=5)
    year = models.CharField(max_length=5)
    pages = models.IntegerField()
    rating = models.FloatField()
    cove = models.TextField()
    description = models.TextField()

