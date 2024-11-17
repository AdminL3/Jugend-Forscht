import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


connection = sqlite3.connect("Analysing/Articlecount/articlecount.db")
cursor = connection.cursor()

colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]
for i, topic in enumerate(topics):
    cursor.execute(f"SELECT * FROM monthly_totals WHERE topic_id = {i}")
    rows = cursor.fetchall()

    # Create DataFrame
    Dataframe = pd.DataFrame(
        rows, columns=[column[0] for column in cursor.description])

    # Drop unnecessary columns
    Dataframe = Dataframe.drop(columns=['id'])
    Dataframe = Dataframe.drop(columns=['topic_id'])

    # Combine 'year' and 'month' into a 'date' column
    Dataframe['date'] = pd.to_datetime(
        Dataframe[['year', 'month']].assign(day=1))

    # Set 'date' as the index
    Dataframe.set_index('date', inplace=True)

    # Plot the article counts by month
    plt.plot(Dataframe.index,
             Dataframe['total_count'], 'o', markersize=4, color=colors[i])

    X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
    y = Dataframe['total_count']
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    plt.plot(Dataframe.index, y_pred, color=colors_reg[i])

    # Customize the plot
    legend1 = [f"Article Count for {topic}"]
    legend2 = [f"Regression Line for {topic}"]
    plt.xlabel("Date")
    plt.ylabel("Article Count")
    plt.legend(legend1 + legend2)
    plt.title(f"Monthly Analysis of Amount of Articles for {topic}")
    plt.tight_layout()

    # Save the plot
    plt.savefig(f"Analysing/Articlecount/output/month/{topic}.png")

    plt.close()


# both

for i in range(len(topics)):
    cursor.execute(f"SELECT * FROM monthly_totals WHERE topic_id = {i}")
    rows = cursor.fetchall()

    # Create DataFrame
    Dataframe = pd.DataFrame(
        rows, columns=[column[0] for column in cursor.description])

    # Drop unnecessary columns
    Dataframe = Dataframe.drop(columns=['id'])
    Dataframe = Dataframe.drop(columns=['topic_id'])

    # Combine 'year' and 'month' into a 'date' column
    Dataframe['date'] = pd.to_datetime(
        Dataframe[['year', 'month']].assign(day=1))

    # Plot the article counts by month
    plt.plot(Dataframe.index,
             Dataframe['total_count'], 'o', markersize=4, color=f'{colors[i]}')

for i, topic in enumerate(topics):
    cursor.execute(f"SELECT * FROM monthly_totals WHERE topic_id = {i}")
    rows = cursor.fetchall()

    Dataframe = pd.DataFrame(
        rows, columns=[column[0] for column in cursor.description])

    Dataframe = Dataframe.drop(columns=['id'])
    Dataframe = Dataframe.drop(columns=['topic_id'])

    Dataframe['date'] = pd.to_datetime(
        Dataframe[['year', 'month']].assign(day=1))

    X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
    y = Dataframe['total_count']
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    plt.plot(Dataframe.index, y_pred, color=colors_reg[i])
# Customize the plot
legend1 = [f"Article Count for {topic}" for topic in topics]
legend2 = [f"Regression Line for {topic}" for topic in topics]
plt.xlabel("Date")
plt.ylabel("Article Count")
plt.legend(legend1 + legend2)
plt.title(f"Monthly Analysis of Amount of Articles")
plt.tight_layout()

# Save the plot
plt.savefig(f"Analysing/Articlecount/output/Month/Both.png")

plt.close()
