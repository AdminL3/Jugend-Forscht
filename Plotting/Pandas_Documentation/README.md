# How to Create Plots in Pandas🐼

- Creating a Function to graph the data
- See the function here: [`Plotting.py`](../Plotting.py)

> [!NOTE]
> If you want a simple introduction to Pandas, without the function, you can find it [here](./simple.md)

---

## Input

- What do we need to create a plot?

```python
def graph(rows, column_names, name, legend_title, title, drop_columns, color, color_reg, regression, size, output):
```

Above is the function signature
We need the following parameters:

- **rows**: The data to be plotted
- **column_names**: The names of the columns
- **name**: The name of the data to be plotted
- **legend_title**: The title of the legend
- **title**: The title of the plot
- **drop_columns**: Columns to be dropped
- **color**: The color of the scatter plot
- **color_reg**: The color of the regression line
- **regression**: Whether to plot the regression line
- **size**: The size of the markers
- **output**: The output file

---

## Creating the Plot

#### Create a DataFrame

- using the given rows and column names

```python
Dataframe = pd.DataFrame(rows, columns=column_names)
```

---

#### Drop Columns

- Drop the columns that are not needed

```python
    for col in drop_columns:
        if col in Dataframe.columns:
            Dataframe = Dataframe.drop(columns=[col])
```

---

#### Convert the date column to datetime

- Convert the date column to datetime

```python
if 'date' in Dataframe.columns:
        Dataframe['date'] = pd.to_datetime(Dataframe['date'])
        Dataframe.set_index('date', inplace=True)
    else:
        Dataframe['date'] = pd.to_datetime(
            Dataframe[['year', 'month']].assign(day=1))
        Dataframe.set_index('date', inplace=True)
```

---

#### Plot the Data

```python
plt.plot(Dataframe.index, Dataframe[name], 'o', markersize=size, color=color)
```

---

#### Plot the Regression Line

```python
if regression:
    ...
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    plt.plot(Dataframe.index, y_pred, color=color_reg)
```

---

#### Update the Legend and title

```python
plt.xticks(rotation=25)
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.2)

plt.xlabel("Date")
plt.ylabel(name.capitalize())
legend = [legend_title, "Regression Line"] if regression else [legend_title]
plt.legend(legend)
plt.text(0, 1.07, title, fontsize=14, verticalalignment='top',
             horizontalalignment='left', transform=plt.gca().transAxes)
```

---

#### Save the Plot

```python
plt.savefig(output)
plt.close()
```

---

## Accessing the function

- Used Example: [`Wordcount`](../Wordcount/)

#### Import the function

```python
from Analysing.Plotting import graph
```

### Prepare the data

##### Set up the values

```python
colors = ['#1f77b4', '#ff7f0e', "green"]
colors_reg = ['blue', 'red', "black"]
topics = ["Politics", "World", "Opinion"]
news = ["NYT", "Guardian"]
```

##### Get the Data from the Database

- Access the database for each newspaper

```python
for n, new in enumerate(news):
    connection = sqlite3.connect(f"Database/Wordcount/{new}.db")
    cursor = connection.cursor()
```

- Loading the data

```python
for i in range(len(topics)):
    cursor.execute(f"SELECT * FROM {topic};")
    rows = cursor.fetchall()
```

- Close connection

```python
connection.close()
```

##### Specificy the parameters

- Set the colors for each topic

```python
    for i in range(len(topics)):
        topic = topics[i]
        color = colors[i]
        regression_color = colors_reg[i]
```

- Set output file

```python
output = f"Output/Wordcount/Graphs/{new}/{topic}.png"
os.makedirs(os.path.dirname(output), exist_ok=True)
```

- Create column names

```python
columns = [column[0] for column in cursor.description]
```

### Create the Plot

- Call the function

```python
graph(
    rows=rows,
    column_names=columns,
    name="wordcount",
    title1=f"Wordcount of {topic}",
    title2=f"Wordcount of {topic}",
    drop_columns=drop_columns,
    color=color,
    color_reg=regression_color,
    regression=True,
    size=2,
    output=output
)
```
