# Generated by Django 2.2.19 on 2022-12-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20221206_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]
