import os
from datetime import datetime
from glob import glob

# Directory where the articles are stored
base_dir = r"data/articles/"

# Define the range of years, months, and topics to check
topics = ["politics", "world"]  # Customize based on your structure
year_range = range(2020, 2022)
month_range = range(1, 13)
# Max days in a month; we'll handle non-existent days in the script
day_range = range(1, 32)

# List of files to skip
files_to_skip = [
    "politics/2021/month08/2021_08_01",
    "politics/2021/month12/2021_12_25",
    "politics/2021/month12/2021_12_31"
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
                    if f"{topic}/{year}/month{month:02}/{year}_{month:02}_{day:02}" in files_to_skip:
                        continue

                except ValueError:
                    continue  # Skip invalid dates

                # Create the file pattern to check for any file with this date
                file_pattern = os.path.join(base_dir, topic, str(year), f"month{
                                            month:02}", f"{year}_{month:02}_{day:02}_*.txt")

                # Check if any file exists for this date
                if not glob(file_pattern):
                    missing_dates.append(
                        f"{topic}/{year}/month{month:02}/{year}_{month:02}_{day:02}")


with open("data-collection/other/missing_files.txt", "w") as f:
    for date in missing_dates:
        f.write(date + "\n")
