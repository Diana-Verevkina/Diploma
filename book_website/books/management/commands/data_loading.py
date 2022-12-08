import csv
import pandas as pd
from django.core.management import BaseCommand
from sklearn.metrics.pairwise import cosine_similarity

from ...models import Author, Book
from sklearn.feature_extraction.text import CountVectorizer

main_path = ('/Users/dianaverevkina/Diplom_project/Diploma — копия 3/'
             'data_preparation')

path = f'{main_path}/clean_data.csv'
path_authors = f'{main_path}/authors_new.csv'
path_tags = f'{main_path}/spacylem.csv'

clean_data = pd.read_csv(f'{main_path}/clean_data.csv')
spacylem = pd.read_csv(f'{main_path}/spacylem.csv')

clean_data['tags'] = spacylem['tags']
dataclean_tags = clean_data
dataclean_tags.to_csv(f'{main_path}/dataclean_tags.csv')
path_dataclean_tags = f'{main_path}/dataclean_tags.csv'




def vector():
    count_vectorizer = CountVectorizer(encoding='utf-8')
    data = spacylem
    count_vectorizer.fit(data['tags'])
    vectors = count_vectorizer.fit_transform(data['tags'].values.astype('U'))
    # Непустые значения нулевой строки
    [i for i in vectors.todense()[0].getA1() if i > 0][0:10]
    vectors
    return vectors


class Command(BaseCommand):
    help = 'Загрузка данных в БД из файлов csv'

    def handle(self, *args, **options):
        if Book.objects.exists():
            raise Exception(f'Ошибка. Данные в модель {Book.__name__} '
                            f'уже загружены.')
        else:
            print(f'Загрузка данных в модель {Book.__name__}...')
        for row in csv.DictReader(open(f'{path_dataclean_tags}',
                                       encoding='utf-8')):
            columns = Book(name=row['name'], author=row['author'],
                           section=row['section'], publish=row['publish'],
                           age=row['age'], year=row['year'],
                           pages=row['pages'],
                           rating=row['rating'], cove=row['cove'],
                           description=row['description'], tags=row['tags'])
            columns.save()
        print(f'Данные в модель {Book.__name__} загружены')

        print(f'Загрузка данных в модель {Book.__name__}...')
        for book in Book.objects.all():
            book.vector = vector()[book.id - 1]
            book.save()
        print(f'Vectors загружены')

        if Author.objects.exists():
            raise Exception(f'Ошибка. Данные в модель {Author.__name__} '
                            f'уже загружены.')
        else:
            print(f'Загрузка данных в модель {Author.__name__}...')
        for row in csv.DictReader(open(f'{path_authors}', encoding='utf-8')):
            columns = Author(author_name=row['author'], )
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
