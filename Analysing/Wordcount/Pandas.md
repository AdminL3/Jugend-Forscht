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

![Quick Data Overview Plot](https://pandas.pydata.org/docs/_images/04_airqual_quick.png)

### Plotting Data for Paris

To focus on data from a single column (e.g., Paris station), use the following:

```python
# Plot only Paris station data
air_quality["station_paris"].plot()
plt.show()
```

![Paris Station Data Plot](https://pandas.pydata.org/docs/_images/04_airqual_paris.png)

## Comparative Plot: London vs. Paris

We can visually compare NO₂ values between London and Paris using a scatter plot:

```python
# Scatter plot for London vs Paris NO₂ levels
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()
```

![Scatter Plot London vs Paris](https://pandas.pydata.org/docs/_images/04_airqual_scatter.png)

## Other Plot Types in Pandas

Aside from line plots, pandas provides several other plotting options. Here’s how to list them:

```python
# List available plot methods in pandas
[method_name for method_name in dir(air_quality.plot) if not method_name.startswith("_")]
```

## Separate Subplots for Each Column

To display each column in a separate subplot, use the `subplots=True` argument:

```python
# Area plot with separate subplots for each station
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
```

![Separate Subplots](https://pandas.pydata.org/docs/_images/04_airqual_area_subplot.png)

## Customizing and Saving Plots

For further customization, we can interact directly with the Matplotlib figure and axes:

```python
# Customize plot with labels and save to file
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO₂ concentration")
fig.savefig("no2_concentrations.png")
plt.show()
```

![Customized Plot](https://pandas.pydata.org/docs/_images/04_airqual_customized.png)

> **Remember**:
>
> - `.plot.*` methods work on both Series and DataFrames.
> - Each column is plotted as a different element (e.g., line, boxplot).
> - Pandas plots are Matplotlib objects, so you can fully customize them with Matplotlib.

---
