import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

connection = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = connection.cursor()


cursor.execute("SELECT * FROM Politics;")
politics_rows = cursor.fetchall()
cursor.execute("SELECT * FROM World;")
world_rows = cursor.fetchall()


DataframePolitics = pd.DataFrame(
    politics_rows, columns=[column[0] for column in cursor.description])
DataframeWorld = pd.DataFrame(
    world_rows, columns=[column[0] for column in cursor.description])


DataframePolitics = DataframePolitics.drop(columns=['id'])
DataframeWorld = DataframeWorld.drop(columns=['id'])


DataframePolitics['date'] = pd.to_datetime(DataframePolitics['date'])
DataframePolitics.set_index('date', inplace=True)

DataframeWorld['date'] = pd.to_datetime(DataframeWorld['date'])
DataframeWorld.set_index('date', inplace=True)

plt.plot(DataframePolitics.index,
         DataframePolitics['wordcount'], 'o', markersize=2)
plt.plot(DataframeWorld.index,
         DataframeWorld['wordcount'], 'o', markersize=2)


# Step 5: Apply linear regression on both datasets
# Linear regression for Politics
X_politics = DataframePolitics.index.astype(np.int64).values.reshape(-1, 1)
y_politics = DataframePolitics['wordcount']
model_politics = LinearRegression()
model_politics.fit(X_politics, y_politics)
y_pred_politics = model_politics.predict(X_politics)
plt.plot(DataframePolitics.index, y_pred_politics,
         color='red')

# Linear regression for World
X_world = DataframeWorld.index.astype(np.int64).values.reshape(-1, 1)
y_world = DataframeWorld['wordcount']
model_world = LinearRegression()
model_world.fit(X_world, y_world)
y_pred_world = model_world.predict(X_world)
plt.plot(DataframeWorld.index, y_pred_world,
         color='blue')

# Step 6: Add labels, legend, and title
plt.xlabel("Date")
plt.ylabel("Word Count")
plt.legend(["Politics Word Count", "World Word Count",
           "Politics Regression Line", "World Regression Line"])
plt.title("Word Count Analysis for Politics and World")

# Step 7: Save the plot as an image
plt.savefig("Analysing\Wordcount\Pandas_Documentation\img4.png")

# Display the plot
plt.show()
