# Generated by Django 2.2.19 on 2022-12-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_author_author_name_lower'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
