import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

connection = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = connection.cursor()

name = "All"
color = "#339933"
color_reg = "#000"
topics = ["politics", "world", "opinion"]

rows = []
for topic in topics:
    cursor.execute(f"SELECT * FROM {topic};")
    rows.extend(cursor.fetchall())


Dataframe = pd.DataFrame(
    rows, columns=[column[0] for column in cursor.description])


Dataframe = Dataframe.drop(columns=['id'])
Dataframe = Dataframe.drop(columns=['idx'])

Dataframe['date'] = pd.to_datetime(Dataframe['date'])
Dataframe.set_index('date', inplace=True)

Dataframe.plot(style='o', markersize=2, color=f'{color}')


X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
y = Dataframe['wordcount']
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
plt.plot(Dataframe.index, y_pred, color=f'{color_reg}')


plt.xlabel("Date")
plt.ylabel("")
plt.legend([f"{name} Word Count", "Regression Line"])
plt.title(f"Word Count Analysis - {name}")
plt.savefig(f"Analysing\Wordcount\output\{name}.png")

plt.close()
