import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


path_books = ('/Users/dianaverevkina/Diplom_project/Diploma — копия 3/'
              'data_preparation/spacylem.csv')


def recommend(enter_book):
    books = pd.read_csv(path_books)
    count_vectorizer = CountVectorizer(encoding='utf-8')
    count_vectorizer.fit(books['tags'])
    vectors = count_vectorizer.fit_transform(books['tags'].values.astype('U'))
    similarity = cosine_similarity(vectors)
    enter_book_index = books[books['name'] == enter_book].index[0]
    distances = sorted(list(enumerate(similarity[enter_book_index])),
                       reverse=True, key=lambda x: x[1])
    recommended_book_names = []
    for i in distances[1:9]:
        recommended_book_names.append(books.name[books.iloc[i[0]].name])
    return recommended_book_names
