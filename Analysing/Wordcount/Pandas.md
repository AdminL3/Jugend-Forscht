# How to Create Plots in Pandas

## Data Preparation

We will start by importing the necessary libraries and loading the data.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the air quality data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.head()
```

> **Note**: `index_col=0` sets the first column as the DataFrame index, and `parse_dates=True` converts dates into `Timestamp` objects.

## Plotting Basics

### Quick Visual Check of the Data

```python
# Quick overview plot
air_quality.plot()
plt.show()
```

Pandas creates one line plot for each numeric column by default.

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
