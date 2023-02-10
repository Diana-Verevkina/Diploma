# Generated by Django 2.2.16 on 2023-02-10 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20230115_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='section_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='books.Section', verbose_name='Section'),
        ),
    ]
