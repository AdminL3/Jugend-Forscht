# This is only the Graph Documentation from ChatGPT for later

This Python script is designed to traverse a nested directory structure containing time-series data in text files, read numerical values from each file, and plot the data over time with a linear regression line. Additionally, it identifies and displays the top 5 points with the largest deviations from the regression line.

## Requirements

This script requires the following Python libraries:

- `os`
- `pandas`
- `matplotlib`
- `numpy`

Ensure these are installed by running:

```bash
pip install pandas matplotlib numpy
```

## Directory Structure

The script expects a specific directory structure. The root directory should contain subdirectories for each year, within which there should be subdirectories for each month (prefixed with "month") and within those, subdirectories for each day (prefixed with "day"). Each day directory contains text files with numerical data.

### Example Directory Structure

```plaintext
data\word_count\politics\
    ├── 2020\
    │   └── month01\
    │       └── day01\
    │           └── 1.txt (contains a single numerical value)
    ├── 2021\
    │   └── month02\
    │       └── day15\
    │           └── 1.txt
    ...
```

## Usage

### Code Walkthrough

1. **Directory Traversal**:

   - The script traverses the nested directory structure using `os.listdir()` and filters directories for valid years, months, and days.
   - For each text file found, it reads the content, attempts to convert it to a floating-point number, and adds it to a list of data points.

2. **Data Collection**:

   - A list named `data` is populated with tuples containing the date (in `YYYY-MM-DD` format) and the numerical value read from each file.

3. **DataFrame Creation**:

   - The collected data is loaded into a `pandas` DataFrame with columns `Date` and `Value`.
   - Invalid dates are dropped, and the DataFrame is sorted by date.

4. **Plotting**:

   - A scatter plot of the `Value` data over time is created.
   - A linear regression line is calculated and overlaid on the scatter plot.

5. **Deviation Calculation**:

   - The deviation of each data point from the regression line is calculated.
   - The top 5 points with the highest deviation are identified and displayed in the console.

6. **Display**:
   - The script displays the plot with the data points and the regression line.

### Code Snippet

Below is a summary of key code segments for each step:

#### 1. Directory Traversal

```python
for year in os.listdir(root_dir):
    # Further filtering and reading data files
```

#### 2. Data Collection

```python
data.append((date_str, number))
```

#### 3. DataFrame Creation

```python
df = pd.DataFrame(data, columns=['Date', 'Value'])
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna().sort_values('Date')
```

#### 4. Plotting and Regression Line

```python
plt.scatter(df['Date'], df['Value'], color='b', label='Data Points')
slope, intercept = np.polyfit(x_values, df['Value'], 1)
regression_line = slope * x_values + intercept
plt.plot(df['Date'], regression_line, color='red', label='Regression Line')
```

#### 5. Top Deviations

```python
df['Deviation'] = abs(df['Value'] - df['Regression_Pred'])
top_5_deviations = df.nlargest(5, 'Deviation')
print("Top 5 points with highest deviation from regression line:")
print(top_5_deviations[['Date', 'Value', 'Deviation']])
```

### Example Output

1. **Console Output**:

   - The console will display the top 5 points with the highest deviation from the regression line, formatted as a table of `Date`, `Value`, and `Deviation`.

2. **Plot**:
   - A scatter plot of the data points over time with the regression line will be displayed. Data points with larger deviations will visually differ from the regression line.

### Notes

- **Error Handling**:

  - If a file does not contain a valid number, it will print a message indicating that the file was skipped.

- **Dependencies**:
  - Ensure `matplotlib`, `pandas`, and `numpy` are installed.

### Future Improvements

- **File Validation**:
  - Enhance error handling for various file formats or malformed data.
- **Data Filtering**:
  - Add options to filter or group data by month or year.

---

This documentation provides an overview of the script, an explanation of its core functionality, and an example of its usage. It also includes code snippets for each major section, example output, and suggestions for improvements.
