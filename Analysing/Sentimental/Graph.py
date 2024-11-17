import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyparsing import col
from sklearn.linear_model import LinearRegression

connection = sqlite3.connect("Analysing\Sentimental\sentiment.db")
cursor = connection.cursor()

colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]

options = ['polarity', 'subjectivity']
for o, option in enumerate(options):
    name = option.capitalize()
    for i, topic in enumerate(topics):
        cursor.execute(f"SELECT * FROM {topic};")
        rows = cursor.fetchall()

        Dataframe = pd.DataFrame(
            rows, columns=[column[0] for column in cursor.description])

        Dataframe = Dataframe.drop(columns=['id'])
        Dataframe = Dataframe.drop(columns=[f'{options[1-o]}'])

        Dataframe['date'] = pd.to_datetime(Dataframe['date'])
        Dataframe.set_index('date', inplace=True)

        Dataframe.plot(style='o', markersize=2, color=f'{colors[i]}')

        # Regression
        X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
        y = Dataframe[f'{option}']
        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)
        plt.plot(Dataframe.index, y_pred, color=f'{colors_reg[i]}')

        plt.xlabel("Date")
        plt.ylabel("")
        plt.legend([f"{name} for {topic}", f"Regression Line"])
        plt.title(f"{name} Analysis for {topic}")
        plt.savefig(f"Analysing/Sentimental/output/{option}/{topic}.png")

        plt.close()
