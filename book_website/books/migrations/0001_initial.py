# Generated by Django 2.2.19 on 2022-07-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
                ('publish', models.CharField(default=None, max_length=50)),
                ('age', models.CharField(max_length=5)),
                ('year', models.CharField(max_length=5)),
                ('pages', models.IntegerField()),
                ('rating', models.FloatField(blank=True, null=True)),
                ('cove', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
