# Generated by Django 3.2.18 on 2023-05-07 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20230210_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(max_length=50, verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='authors/', verbose_name='Фото автора'),
        ),
        migrations.AlterField(
            model_name='book',
            name='age',
            field=models.CharField(max_length=10, verbose_name='Возрастное ограничение'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Описание книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='books/', verbose_name='Обложка книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Количество страниц'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='book',
            name='section',
            field=models.CharField(max_length=50, verbose_name='Название секции'),
        ),
        migrations.AlterField(
            model_name='book',
            name='section_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='books.section', verbose_name='Секция'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.CharField(max_length=10, verbose_name='Год издания'),
        ),
    ]