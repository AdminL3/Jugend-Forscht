# Analysing the NYT data

- The data, which we collected in [Step 2: # Data Collection from the NYT](../data-collection/)

---

## Get the Data

This is used in every step.

- This step involves collecting the articles created before.
- This depends on your file structure!
- My file structure:

```bash
data/articles/<topic>/<year>/month<month>/day<day>/<index>.txt
```

---

## Option 1: Analysing Wordcount

See [Wordcount.py](./Wordcount/)

- Counting The Words
- Visualizing them in a Graph
- Extracting longest articles based on regression line
- Getting Korrelation Koefficient

---

## Result

- This is only a part of the full project!

- The part, where we analyse the data.

- View the whole Projekt at [Github](https://github.com/AdminL3/Jugend-Forscht/)

Sure, here's a documentation in markdown style for the code snippet you provided:

# Analysing/Graph.py

This script is used to generate a scatter plot of data points and a regression line. The data points are collected from text files in a specific directory structure. The directory structure is as follows:

The script collects data from all the text files in the directory structure and stores it in a pandas DataFrame. The DataFrame has two columns: 'Date' and 'Value'. The 'Date' column contains the date in the format 'YYYY-MM-DD' and the 'Value' column contains the numerical value from the text file.

The script then performs the following steps:

1. Converts the 'Date' column to datetime format.
2. Sorts the DataFrame by the 'Date' column.
3. Plots the data points as scatter points without lines.
4. Creates a regression line using numpy's polyfit function.
5. Calculates the deviation of each data point from the regression line.
6. Identifies the top 5 data points with the highest deviation.
7. Prints the top 5 data points and their deviation.
8. Adds labels, title, grid, and rotates x-axis labels.

The resulting plot shows the data points and the regression line.

Please note that the script assumes that the text files in the directory structure contain a single numerical value. If the files contain multiple values or non-numerical data, the script may not work as expected.

Let me know if you need any further assistance.
