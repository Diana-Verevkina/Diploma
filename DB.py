import pandas as pd
import json
# import sqlite


with open('project_book.json', encoding="utf-8") as file:
    data = json.load(file)

# Create A DataFrame From the JSON Data
df = pd.DataFrame(data)

