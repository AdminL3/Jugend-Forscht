import os
from datetime import datetime


news = ["NYT", "Guardian"]
topics = ["politics", "world", "opinion"]
year_range = range(2020, 2022)
month_range = range(1, 13)
day_range = range(1, 32)


missing_dates = []
for news_source in news:
    # Iterate over each topic, year, month, and day
    for topic in topics:
        for year in year_range:
            for month in month_range:
                for day in day_range:
                    try:
                        # Validate date to handle non-existent days like February 30
                        date_str = f"{year}_{month:02}_{day:02}"
                        datetime.strptime(date_str, "%Y_%m_%d")

                        path = f"data/{news_source}/articles/{
                            topic}/{year}/month{month:02}/day{day:02}"

                        # Check if directory exists and contains any files
                        if not os.path.exists(path) or not os.listdir(path):
                            missing_dates.append(
                                f"data/{news_source}/articles/{topic}/{
                                    year}/month{month:02}/day{day:02}/"
                            )

                    except ValueError:
                        continue  # Skip invalid dates

    # Write missing dates to file
    with open("data-collection/Missing Files/missing_files.txt", "w") as f:
        for date in missing_dates:
            f.write(date + "\n")
