import pickle
import pandas as pd


def recommend(rusbook):
    books_dict = pickle.load(
        open('/Users/dianaverevkina/Diplom_project/Diploma/books_dict.pkl',
             'rb'))
    books = pd.DataFrame(books_dict)
    similarity = pickle.load(
        open('/Users/dianaverevkina/Diplom_project/Diploma/similarity.pkl',
             'rb'))
    rusbook_index = books[books['name'] == rusbook].index[0]
    distances = sorted(list(enumerate(similarity[rusbook_index])), reverse=True,
                       key=lambda x: x[1])
    recommended_book_names = []
    for i in distances[1:9]:
        recommended_book_names.append(books.name[books.iloc[i[0]].name])
    return recommended_book_names


recommended_book_names = recommend('Психолог в концлагере ')
print(recommended_book_names)
