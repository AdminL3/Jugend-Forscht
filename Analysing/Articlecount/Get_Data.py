import os
import json

start_year = 2020
amount_years = 2
topics = ["politics", "world"]

# Dictionary to hold article counts
article_count = {}

for topic in topics:
    print(f"Processing topic: {topic}")
    article_count[topic] = {}
    for i in range(amount_years):
        year = start_year + i
        print(f"  Year: {year}")
        # Adding a 'total' key for the year
        article_count[topic][year] = {"months": {}, "total": 0}
        for j in range(12):
            month = str(j + 1).zfill(2)
            print(f"    Month: {month}")
            files_path = f"data/articles/{topic}/{year}/month{month}/"
            monthly_total = 0  # To count articles for the current month

            if os.path.exists(files_path):
                month_days = os.listdir(files_path)
                article_count[topic][year]["months"][month] = {
                    "days": {}, "total": 0}

                for day in month_days:
                    day_path = os.path.join(files_path, day)
                    if os.path.isdir(day_path):
                        files = [file for file in os.listdir(
                            day_path) if file.endswith('.txt')]
                        daily_count = len(files)
                        article_count[topic][year]["months"][month]["days"][day] = daily_count
                        monthly_total += daily_count  # Update monthly total

                # Save the total articles for the month
                article_count[topic][year]["months"][month]["total"] = monthly_total
            else:
                print(f"Folder does not exist: {files_path}")

            # Add the monthly total to the yearly total
            article_count[topic][year]["total"] += monthly_total

# Save article count data to a JSON file
output_file = "article_count_with_totals.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(article_count, f, indent=4, ensure_ascii=False)

print(f"Article count data saved to {output_file}")
