import colorsys
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyparsing import col
from sklearn.linear_model import LinearRegression

connection = sqlite3.connect("Analysing\Sentimental\sentiment.db")
cursor = connection.cursor()

title = "All"
color = "#339933"
color_reg = "#000"
topics = ["Politics", "World", "Opinion"]
options = ['polarity', 'subjectivity']
for o, option in enumerate(options):
    name = option.capitalize()
    rows = []
    for i, topic in enumerate(topics):
        cursor.execute(f"SELECT * FROM {topic};")
        rows.extend(cursor.fetchall())

    Dataframe = pd.DataFrame(
        rows, columns=[column[0] for column in cursor.description])

    Dataframe = Dataframe.drop(columns=['id'])
    Dataframe = Dataframe.drop(columns=['idx'])
    Dataframe = Dataframe.drop(columns=[f'{options[1-o]}'])

    Dataframe['date'] = pd.to_datetime(Dataframe['date'])
    Dataframe.set_index('date', inplace=True)

    Dataframe.plot(style='o', markersize=2, color=f'{color}')

    # Regression
    X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
    y = Dataframe[f'{option}']
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    plt.plot(Dataframe.index, y_pred, color=f'{color_reg}')

    plt.xlabel("Date")
    plt.ylabel("")
    plt.legend([f"{name} for {title}", f"Regression Line"])
    plt.title(f"{name} Analysis for {title}")
    plt.savefig(f"Analysing/Sentimental/output/{option}/{title}.png")

    plt.close()
