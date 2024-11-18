import os
# Save your API key in a file called config.py
import config
import requests


start_year = 2020
amount_years = 1
topics = ["world"]
start_month = 12
amount_month = 1

last_date = 0
api_key = config.APIKEY
for topic in topics:
    for i in range(amount_years):
        year = start_year + i
        for i in range(amount_month):
            month = start_month + i
            urls_path = f"data/links/{topic}/{year}/month{month}.txt"
            with open(urls_path, 'r', encoding='utf-8') as file:
                urls = file.read().splitlines()
            index = 0
            for url in urls:

                parts = url.split('/')
                year = parts[3]
                month = parts[4]
                day = parts[5]
                date = f"{year}_{month}_{day}_"
                if last_date == date:
                    index += 1
                else:
                    index = 1
                file_name = f"{date}{index}.txt"

                output_dir = f"data/source/{topic}/{year}/month{month}/"
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, file_name)
                if os.path.exists(output_file):
                    print(f"File {file_name} already exists. Skipping...")
                    last_date = date
                    continue

                payload = {'api_key': api_key,
                           'url': url}
                r = requests.get('https://api.scraperapi.com/', params=payload)

                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(r.text)

                print("Saved to " + output_file)

                last_date = date


print("Finished saving:")
print(f"Year {str(start_year)} to year {str(start_year + amount_years - 1)}")
print(f"Month {str(start_month)} to month {
      str(start_month + amount_month - 1)}")
print("and Topics " + str(topics))
