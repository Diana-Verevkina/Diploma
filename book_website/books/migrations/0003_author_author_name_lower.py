# Generated by Django 2.2.16 on 2022-11-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_name_lower'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_name_lower',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]