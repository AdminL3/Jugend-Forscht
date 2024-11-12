import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

connection = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM Wordcount;")
rows = cursor.fetchall()
Dataframe = pd.DataFrame(
    rows, columns=[column[0] for column in cursor.description])

Dataframe = Dataframe.drop(columns=['id'])

Dataframe.plot(style='o', markersize=2)

plt.legend(['Wordcount'])

plt.savefig("Analysing\Wordcount\docs\img2.png")

plt.show()


connection.close()
