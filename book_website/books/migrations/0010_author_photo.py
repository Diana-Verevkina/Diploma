# Generated by Django 2.2.19 on 2022-08-21 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20220821_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, upload_to='authors/', verbose_name='Картинка'),
        ),
    ]