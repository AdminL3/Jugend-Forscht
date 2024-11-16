import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

connection = sqlite3.connect("Analysing\Sentimental\sentiment.db")
cursor = connection.cursor()


topic = "Politics"
cursor.execute(f"SELECT * FROM {topic};")
rows = cursor.fetchall()


Dataframe = pd.DataFrame(
    rows, columns=[column[0] for column in cursor.description])


Dataframe = Dataframe.drop(columns=['id'])
Dataframe = Dataframe.drop(columns=['polarity'])

Dataframe['date'] = pd.to_datetime(Dataframe['date'])
Dataframe.set_index('date', inplace=True)

Dataframe.plot(style='o', markersize=2)

# Regression
X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
y = Dataframe['subjectivity']
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
plt.plot(Dataframe.index, y_pred, color='red')


plt.xlabel("Date")
plt.ylabel("")
plt.legend(["Subjectivity", "Regression Line"])
plt.title("Subjectivity Analysis")
plt.savefig(f"Analysing/Sentimental/output/subjectivity/{topic}.png")

plt.close()
