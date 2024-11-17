import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

connection = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = connection.cursor()

topics = ["Politics", "World"]
# topics = ["Politics", "World", "Opinion"]
colors = ['#1f77b4', '#ff7f0e']
colors_reg = ['red', 'blue']


for i, topic in enumerate(topics):
    # set variables
    topic = topics[i]
    color = colors[i]
    regression_color = colors_reg[i]

    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()

    Dataframe = pd.DataFrame(
        rows, columns=[column[0] for column in cursor.description])

    Dataframe = Dataframe.drop(columns=['id'])

    Dataframe['date'] = pd.to_datetime(Dataframe['date'])
    Dataframe.set_index('date', inplace=True)

    plt.plot(Dataframe.index,
             Dataframe['wordcount'], 'o', markersize=2, color=f'{color}')

    X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
    y = Dataframe['wordcount']
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    plt.plot(Dataframe.index, y_pred, color=f'{regression_color}')

# Step 6: Add labels, legend, and title
legend1 = [f"Word Count for {topic}" for topic in topics]
legend2 = [f"Regression Line for {topic}" for topic in topics]

legend = [item for pair in zip(legend1, legend2) for item in pair]


plt.xlabel("Date")
plt.ylabel("Word Count")
plt.legend(legend)
plt.title("Word Count Analysis")

# Step 7: Save the plot as an image
plt.savefig("Analysing\Wordcount\output\Both.png")

# Display the plot
plt.show()
