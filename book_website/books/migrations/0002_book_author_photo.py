# Generated by Django 2.2.19 on 2022-07-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_photo',
            field=models.TextField(blank=True, null=True),
        ),
    ]