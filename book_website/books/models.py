from django.db import models


class books_book(models.Model):
    index = models.IntegerField(default=None)
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

"""

from django.db import models


class Books(models.Model):
    index = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    author = models.TextField(blank=True, null=True)  # This field type is a guess.
    section = models.TextField(blank=True, null=True)  # This field type is a guess.
    publish = models.TextField(blank=True, null=True)  # This field type is a guess.
    age = models.TextField(blank=True, null=True)  # This field type is a guess.
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    cove = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.

"""


