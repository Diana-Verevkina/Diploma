# Generated by Django 2.2.19 on 2022-12-07 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_book_vector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_photo',
        ),
        migrations.RemoveField(
            model_name='book',
            name='is_favore',
        ),
    ]
