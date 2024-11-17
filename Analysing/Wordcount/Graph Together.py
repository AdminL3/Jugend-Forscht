from operator import le
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

connection = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = connection.cursor()

colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]

for i, topic in enumerate(topics):
    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()

    Dataframe = pd.DataFrame(
        rows, columns=[column[0] for column in cursor.description])

    Dataframe = Dataframe.drop(columns=['id'])
    Dataframe['date'] = pd.to_datetime(Dataframe['date'])
    Dataframe.set_index('date', inplace=True)

    plt.plot(Dataframe.index,
             Dataframe['wordcount'], 'o', markersize=1, color=colors[i])


for i, topic in enumerate(topics):
    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()

    Dataframe = pd.DataFrame(
        rows, columns=[column[0] for column in cursor.description])

    Dataframe = Dataframe.drop(columns=['id'])
    Dataframe['date'] = pd.to_datetime(Dataframe['date'])
    Dataframe.set_index('date', inplace=True)

    X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
    y = Dataframe['wordcount']
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    plt.plot(Dataframe.index, y_pred, color=colors_reg[i])

legend1 = [f"Word Count for {topic}" for topic in topics]
legend2 = [f"Regression Line for {topic}" for topic in topics]
plt.xlabel("Date")
plt.ylabel("Word Count")
plt.legend(legend1 + legend2)
plt.title("Word Count Analysis")

plt.savefig("Analysing\Wordcount\output\Both.png")
plt.show()
