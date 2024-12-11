import datetime
import multiprocessing
import os
import re
import time
import requests


patterns = [
    r'theguardian\.com/(?P<topic>[^/]+)/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})',
    r'theguardian\.com/(?P<topic>[^/]+)/[^/]+/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})',
    r'theguardian\.com/[^/]+/(?P<topic>[^/]+)/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})',
    r'theguardian\.com/(?P<topic>[^/]+)/blog/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})',
    r'theguardian\.com/(?P<topic>[^/]+)/live/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})',
]


def extract_info(url):
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.groupdict()
    return None


def requestss(n):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    error_html = "<head><title>429 Too Many Requests</title></head>"

    start_year = 2010
    amount_years = 1
    topics = ["politics"]
    start_month = n
    amount_month = 1
    last_date = 0
    for topic in topics:
        print(topic)
        for y in range(amount_years):
            yeaar = start_year + y
            print(yeaar)
            for m in range(amount_month):
                month = start_month + m
                print(month)
                urls_path = f"data/Guardian/links/{
                    topic}/{yeaar}/month{month:02}.txt"
                with open(urls_path, 'r', encoding='utf-8') as file:
                    urls = file.read().splitlines()
                index = 0

                for url in urls:
                    info = extract_info(url)
                    if info:
                        day = info.get("day")
                        month = info.get("month")
                        year = info.get("year")
                        typ = info.get("topic")
                    else:
                        print("No match found for URL:", url)

                    month_number = datetime.datetime.strptime(
                        month, "%b").month
                    date = f"{year}_{month_number:02}_{day}"

                    if last_date == date:
                        index += 1
                    else:
                        index = 1
                    file_name = f"{date}_{index}.txt"

                    output_dir = f"data/Guardian/source/{
                        topic}/{year}/month{month_number:02}/"
                    os.makedirs(output_dir, exist_ok=True)
                    output_file = os.path.join(output_dir, file_name)
                    if os.path.exists(output_file):
                        # print(f"File {output_file} already exists. Skipping...")
                        # print(f"URL: {url}")
                        last_date = date
                        continue

                    try:
                        response = requests.get(url, headers=headers)
                        page_source = response.text
                        if error_html not in page_source:
                            with open(output_file, "w", encoding="utf-8") as f:
                                f.write(page_source)
                            print(f"Success {output_file}")
                        else:
                            print(f"Error 429: {url}")
                            time.sleep(2)

                    except requests.exceptions.RequestException as e:
                        print(f"Error fetching webpage: {e}")
                        time.sleep(5)

                    last_date = date


numbers = [9, 10, 11, 12]

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        pool.map(requestss, numbers)
    print("Finished saving")
