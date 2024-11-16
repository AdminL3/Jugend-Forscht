import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

connection = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = connection.cursor()

topics = ["Politics", "World"]
topic = topics[1]
colors = ['#1f77b4', '#ff7f0e']
color = colors[0] if topic == "Politics" else colors[1]
colors_reg = ['red', 'blue']
regression_color = colors_reg[0] if topic == "Politics" else colors_reg[1]


cursor.execute(f"SELECT * FROM {topic};")
rows = cursor.fetchall()


Dataframe = pd.DataFrame(
    rows, columns=[column[0] for column in cursor.description])


Dataframe = Dataframe.drop(columns=['id'])

Dataframe['date'] = pd.to_datetime(Dataframe['date'])
Dataframe.set_index('date', inplace=True)

Dataframe.plot(style='o', markersize=2, color=f'{color}')


X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
y = Dataframe['wordcount']
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
plt.plot(Dataframe.index, y_pred, color=f'{regression_color}')


plt.xlabel("Date")
plt.ylabel("")
plt.legend([f"{topic} Word Count", "Regression Line"])
plt.title(f"Word Count Analysis  - {topic}")
plt.savefig(f"Analysing\Wordcount\output\{topic}.png")

plt.show()
