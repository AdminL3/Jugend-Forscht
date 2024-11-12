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
Dataframe.plot()
plt.show()


fig = plt.gcf()
fig.savefig("Analysing\Wordcount\docs\img1.png")


connection.close()
