import requests
import time
import os
import config

# start variables
start_year = 2020
amount_years = 2

topics = ["world", "politics", "opinion"]
API_KEY = config.NYT_API_KEY

for i in range(amount_years):
    year = start_year + i
    for month in range(1, 13):
        all_files_exist = all(os.path.exists(
            f"data/links/{topic}/{year}/month{month}.txt") for topic in topics)

        if all_files_exist:
            print(f"Files for month {month} in year {
                  year} already exist. Skipping...")
            continue

        URL = f"https://api.nytimes.com/svc/archive/v1/{
            year}/{month}.json?api-key={API_KEY}"
        try:
            # get data
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()
            articles = data.get("response", {}).get("docs", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            time.sleep(5)
            continue
        except ValueError:
            print("Error parsing JSON response.")
            continue

        for topic in topics:
            file_path = f"data/links/{topic}/{year}/month{month}.txt"
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as file:
                for article in articles:
                    url = article.get("web_url", "No URL")
                    if f"/{topic}/" in url:
                        if any(format in url for format in ["/interactive/", "/slideshow/", "/video/", "/crossword/"]):
                            continue
                        file.write(url + '\n')

            print(f"Links for {topic} successfully saved in '{
                  year}/month{month}.txt'.")
            time.sleep(3)
