# Generated by Django 2.2.19 on 2022-07-30 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_author_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
                ('author_photo', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Author', verbose_name='Автор'),
        ),
    ]