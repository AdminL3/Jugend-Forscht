import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Replace with your root directory path
root_dir = r'data\word_count\politics'

# List to store dates and numbers
data = []

# Traverse directories
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
                                        print(f"Skipping invalid data in {
                                              file_path}")

# Check collected data
print("Collected data:", data)

df = pd.DataFrame(data, columns=['Date', 'Value'])
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna().sort_values('Date')

# Plot scatter points without lines
plt.figure(figsize=(10, 6))
plt.scatter(df['Date'], df['Value'], color='b', label='Data Points')

# Create regression line
x_values = np.arange(len(df))
slope, intercept = np.polyfit(x_values, df['Value'], 1)
regression_line = slope * x_values + intercept
plt.plot(df['Date'], regression_line, color='red', label='Regression Line')

# Calculate deviations from the regression line
df['Regression_Pred'] = regression_line
df['Deviation'] = abs(df['Value'] - df['Regression_Pred'])

# Identify the top 5 deviations
top_5_deviations = df.nlargest(5, 'Deviation')
print("Top 5 points with highest deviation from regression line:")
print(top_5_deviations[['Date', 'Value', 'Deviation']])

# Labels and title
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Values Over Time with Regression Line')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
