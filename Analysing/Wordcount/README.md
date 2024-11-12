# Plotting a Graph Using Pandas, Matplotlib, and Numpy

This guide walks through how to plot a time series graph in Python using `pandas`, `matplotlib`, and `numpy` to visualize data and calculate a regression line. The data can be read from either a directory structure of `.txt` files or a database.

### Setup and Import Libraries

First, import the necessary libraries:

```python
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sqlite3
```

### Collect Data from Files

If the data is saved as individual `.txt` files in a directory structure by year, month, and day (e.g., `data\word_count\politics\2020\month01\day01\1.txt`), you can use the following code to traverse and collect the data:

```python
# Define root directory path for file-based data
root_dir = r'data\word_count\politics'

# List to store dates and numbers
data = []

# Traverse directories to collect data
for year in os.listdir(root_dir):
    year_path = os.path.join(root_dir, year)
    if os.path.isdir(year_path) and year.isdigit():
        for month in os.listdir(year_path):
            month_path = os.path.join(year_path, month)
            if os.path.isdir(month_path) and month.startswith("month"):
                month_num = month[5:]
                for day in os.listdir(month_path):
                    day_path = os.path.join(month_path, day)
                    if os.path.isdir(day_path) and day.startswith("day"):
                        day_num = day[3:]
                        for file in os.listdir(day_path):
                            if file.endswith('.txt'):
                                file_path = os.path.join(day_path, file)
                                date_str = f"{year}-{month_num}-{day_num}"

                                with open(file_path, 'r') as f:
                                    try:
                                        number = float(f.read().strip())
                                        data.append((date_str, number))
                                    except ValueError:
                                        print(f"Skipping invalid data in {file_path}")
```

### Collect Data from a Database

If you prefer to read the data from a database instead, use the following code to set up an SQLite database and retrieve data.

#### Step 1: Create the Database and Table

Run this once to create the database and table structure:

```python
# Connect to SQLite database (or create it)
conn = sqlite3.connect('data_analysis.db')
cursor = conn.cursor()

# Create table to store data if not already present
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Data (
        date TEXT PRIMARY KEY,
        value REAL
    )
''')
conn.commit()
```

#### Step 2: Insert Data into the Database

To load existing data into the database, adapt the `data` list from the file traversal code:

```python
# Insert data into the database
for date_str, number in data:
    cursor.execute("INSERT OR REPLACE INTO Data (date, value) VALUES (?, ?)", (date_str, number))
conn.commit()
```

#### Step 3: Retrieve Data from the Database

Use this code to retrieve the data from the database and load it into a `DataFrame`:

```python
# Read data from database
cursor.execute("SELECT date, value FROM Data")
rows = cursor.fetchall()

# Convert data to DataFrame
df = pd.DataFrame(rows, columns=['Date', 'Value'])
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna().sort_values('Date')
```

### Plot the Data

Now that the data is loaded in the `DataFrame`, create a scatter plot to display values over time.

```python
plt.figure(figsize=(10, 6))
plt.scatter(df['Date'], df['Value'], color='b', label='Data Points')
```

### Add a Regression Line

To add a regression line, use `numpy.polyfit` to calculate the slope and intercept, and plot it over the scatter points.

```python
# Generate x-values for regression line
x_values = np.arange(len(df))
slope, intercept = np.polyfit(x_values, df['Value'], 1)
regression_line = slope * x_values + intercept

# Plot regression line
plt.plot(df['Date'], regression_line, color='red', label='Regression Line')
```

### Calculate Deviations

Calculate the deviation of each data point from the regression line and identify the top 5 deviations:

```python
# Calculate deviation from regression line
df['Regression_Pred'] = regression_line
df['Deviation'] = abs(df['Value'] - df['Regression_Pred'])

# Find top 5 deviations
top_5_deviations = df.nlargest(5, 'Deviation')
print("Top 5 points with highest deviation from regression line:")
print(top_5_deviations[['Date', 'Value', 'Deviation']])
```

### Finalize the Plot

Add labels, title, legend, and grid, and rotate x-axis labels for readability.

```python
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Values Over Time with Regression Line')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

This guide provides a complete approach for both file-based and database-based data collection, visualization, and analysis.
