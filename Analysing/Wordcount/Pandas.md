# How to Create Plots in Pandas

## Importing

- First for Getting the data from the Database

```
import sqlite3
```

- Then import modules for Plotting

```
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```

## Getting from database

- Accessing Database from before

```
connection = sqlite3.connect("Analysing\Wordcount\wordcount.db")
cursor = connection.cursor()
```

- Loading data

```
cursor.execute("SELECT * FROM Wordcount;")
rows = cursor.fetchall()
```

- Close connection

```
connection.close()
```

## Plotting Basics

### Quick Visual Representation of the Data

- Create Dataframe

```
Dataframe = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])
```

- Plot Data

```
rows.plot()
plt.show()
```

Pandas automatically does the rest

![Quick Data Overview Plot](docs/img1.png)

### Saving the Plot

```python
plt.savefig("Analysing\Wordcount\docs\img1.png")
```

- Make sure to add this line before **plt.show()**

## Configure Custom Setting

1. The **ID line** is annoying me. Let's remove it

```
Dataframe = Dataframe.drop(columns=['id'])
```

---

2.  Customize **Plotting**:

- Remove Lines
- Reduce Dot Size

```
Dataframe.plot(style='o', markersize=2)
```

instead of:

```
Dataframe.plot()
```

---

4. **Custom Legend**

```
plt.legend(['Wordcount'])
```

---

5. **Custom X-Axis**

```
# Convert date column to datetime
Dataframe['date'] = pd.to_datetime(Dataframe['date'])

# Set the date as the index
Dataframe.set_index('date', inplace=True)

# Update Labels
plt.xlabel("Date")
plt.ylabel("")
```

5. **Custom Title**

```
plt.title("Word Count Analysis")
```

---

- Looks a lot better now:

  ![Result of changes](docs/img2.png)

---

# Regression

#### Prepare Regression

```
pip install scikit-learn
```

#### Prepare data for regression model

```
X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
y = Dataframe['number']
```

#### Set up the model and fit ot

```
model = LinearRegression()
model.fit(X, y)
```

#### Get the parameters

```
y_pred = model.predict(X)
```

#### Plot it

```
plt.plot(Dataframe.index, y_pred, color='red', label='Regression')
```

Make sure to plot the line after you plot the Graph!

#### Update Legend

```
??
```

![Regression](docs/img3.png)
