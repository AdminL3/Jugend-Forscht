import os
import time
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


start_year = 2021
amount_years = 1
topics = ["opinion"]
start_month = 12
amount_month = 1
last_date = 0
for topic in topics:
    for i in range(amount_years):
        year = start_year + i
        for i in range(amount_month):
            month = start_month + i
            print(f"Next Month: {month}")
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

                try:
                    response = requests.get(url)
                    page_source = response.text
                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(page_source)
                        print(page_source)
                        print(f"Success {file_name}")

                except requests.exceptions.RequestException as e:
                    print(f"Error fetching webpage: {e}")
                time.sleep(1)

                last_date = date


print("Finished saving:")
print(f"Year {str(year)} to year {str(start_year + amount_years - 1)}")
print(f"Month {str(month)} to month {str(start_month + amount_month - 1)}")
print("and Topics " + str(topics))
