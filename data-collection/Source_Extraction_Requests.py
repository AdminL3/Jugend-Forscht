import os
import time
import pyperclip
import requests


start_year = 2020
amount_years = 1
topics = ["world"]
monthstart = 2
amount_month = 1
last_date = 0
driver = webdriver.Chrome(options=options)
for topic in topics:
    for i in range(amount_years):
        year = start_year + i
        for i in range(amount_month):
            month = monthstart + i
            print(f"Next Month: {month}")
            urls_path = f"/content/urls/{year}/month{month}.txt"
            # urls_path = f"/content/urls/month1.txt"
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

                output_dir = f"/content/data/NYT/source/{topic}/{year}/month{month}/"
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, file_name)
                if os.path.exists(output_file):
                    print(f"File {file_name} already exists. Skipping...")
                    continue

                driver.get(url)
                time.sleep(1)
                page_source = driver.execute_script("return document.documentElement.outerHTML;")

                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(page_source)
                    print(f"Success {file_name}")


                last_date = date