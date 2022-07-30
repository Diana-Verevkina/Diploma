import pandas as pd
import json
import os
import sqlite3


with open(os.path.join('/Users/dianaverevkina/Diplom_project/Diploma/project_book.json')) as file:
    data = json.load(file)

# Create A DataFrame From the JSON Data
df = pd.DataFrame(data)

conn = sqlite3.connect('data.db')
cur = conn.cursor()
df.to_sql("books_book", conn)

