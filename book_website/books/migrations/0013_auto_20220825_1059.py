# Generated by Django 2.2.19 on 2022-08-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20220824_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]