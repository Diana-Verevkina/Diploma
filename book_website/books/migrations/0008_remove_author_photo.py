# Generated by Django 2.2.19 on 2022-08-21 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20220821_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='photo',
        ),
    ]