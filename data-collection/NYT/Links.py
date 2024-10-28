import requests
import time
import os
import config


year = 2020
month = 0
topics = ["us", "politics", "world"]
API_KEY = config.NYT_API_KEY

for month_idx in range(12):
    month += 1
    file_path = f"data/NYT/links/{topics[0]}/month{month}.txt"
    URL = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={API_KEY}"
    if os.path.exists(file_path):
        print(f"File 'month{month}.txt'  already exists. Skipping...")
        continue
    
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        articles = data.get("response", {}).get("docs", [])
