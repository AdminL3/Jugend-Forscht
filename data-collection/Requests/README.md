# Data Collection Script

This script uses the `requests` library to fetch the source code of web pages and save them to local files. The script iterates over specified topics, years, and months, reads URLs from text files, and saves the fetched HTML content.

## Problems:

- You get blocked really quick, so you have to resort to other methods


## Requirements

- `requests` library

```sh
pip install requests
```

## Usage

#### Setup
```python
import os
import time
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

start_year = 2021
amount_years = 1
topics = ["world"]
start_month = 12
amount_month = 1
last_date = 0
```

#### Loop through links and get code
```
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
```
