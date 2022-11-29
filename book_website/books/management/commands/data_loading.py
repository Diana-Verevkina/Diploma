import csv

from django.core.management import BaseCommand

from ...models import Author, Book

path = '/Users/dianaverevkina/Diplom_project/Diploma — копия/dataclean.csv'
path_authors = '/Users/dianaverevkina/Diplom_project/Diploma/authors_new.csv'


class Command(BaseCommand):
    help = 'Загрузка данных в БД из файлов csv'

    def handle(self, *args, **options):
        """  if Book.objects.exists():
              raise Exception(f'Ошибка. Данные в модель {Book.__name__} '
                              f'уже загружены.')
          else:
              print(f'Загрузка данных в модель {Book.__name__}')"""
        for row in csv.DictReader(open(f'{path}', encoding='utf-8')):
            columns = Book(name=row['name'], author=row['author'],
                           section=row['section'], publish=row['publish'],
                           age=row['age'], year=row['year'],
                           pages=row['pages'],
                           rating=row['rating'], cove=row['cove'],
                           description=row['description'])
            columns.save()
        print(f'Данные в модель {Book.__name__} загружены')

        for row in csv.DictReader(open(f'{path_authors}', encoding='utf-8')):
            columns = Author(author_name=row['author'],)
            columns.save()
        print(f'Данные в модель {Author.__name__} загружены')

        for book in Book.objects.all():
            for author in Author.objects.all():
                if book.author == author.author_name:
                    book.author_id = author
                    book.save()
        print(f'Данные о связях книг с авторами загружены')

        for book in Book.objects.all():
            book.name_lower = book.name.lower().replace(
                ',', '').replace('.', '').replace('...', '').replace(
                '!', '').replace('— ', '').replace('?', '')
            book.save()

        for author in Author.objects.all():
            author.author_name_lower = author.author_name.lower().replace(
                ',', '').replace('.', '').replace('...', '').replace(
                '!', '').replace('— ', '').replace('?', '')
            author.save()
