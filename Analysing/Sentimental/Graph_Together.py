import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyparsing import col
from sklearn.linear_model import LinearRegression

from Analysing.Plotting import multiple

connection = sqlite3.connect("Analysing\Sentimental\sentiment.db")
cursor = connection.cursor()

colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]
options = ['polarity', 'subjectivity']
all_rows = []
all_columns = []
for o, option in enumerate(options):
    for i, topic in enumerate(topics):
        cursor.execute(f"SELECT * FROM {topic};")
        rows = cursor.fetchall()
        all_rows.append(rows)
        all_columns.append([column[0] for column in cursor.description])
    all_titles = ["Politics", "World", "Opinion"]
    drop_columns = ["id", "idx", f'{options[1-0]}']
    size = 2
    output = f"Analysing\Sentimental\output\{option}\Together.png"
    name = option
    regression = True


    multiple(all_rows, all_columns, name, all_titles, drop_columns,
            colors, colors_reg, regression, size, output)