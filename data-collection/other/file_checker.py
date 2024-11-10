import os
from datetime import datetime
from glob import glob

# Directory where the articles are stored
base_dir = r"data/articles/"

# Define the range of years, months, topics to check
topics = ["politics", "world"]  # Customize based on your structure
year_range = range(2020, 2022)
month_range = range(1, 13)
day_range = range(1, 32)

# List of files to skip
files_to_skip = [
    "politics/2021/month08/day01",
    "politics/2021/month12/day25",
    "politics/2021/month12/day31"
]

missing_dates = []

# Iterate over each topic, year, month, and day
for topic in topics:
    for year in year_range:
        for month in month_range:
            for day in day_range:
                try:
                    # Validate date to handle non-existent days like February 30
                    date_str = f"{year}_{month:02}_{day:02}"
                    datetime.strptime(date_str, "%Y_%m_%d")

                    # Skip the specific files mentioned
                    if f"{topic}/{year}/month{month:02}/day{day:02}" in files_to_skip:
                        continue

                    # Create the directory path to check
                    dir_path = os.path.join(
                        base_dir,
                        topic,
                        str(year),
                        f"month{month:02}",
                        f"day{day:02}"
                    )

                    # Check if directory exists and contains any files
                    if not os.path.exists(dir_path) or not os.listdir(dir_path):
                        missing_dates.append(
                            f"{topic}/{year}/month{month:02}/day{day:02}"
                        )

                except ValueError:
                    continue  # Skip invalid dates

# Write missing dates to file
with open("data-collection/other/missing_files.txt", "w") as f:
    for date in missing_dates:
        f.write(date + "\n")
