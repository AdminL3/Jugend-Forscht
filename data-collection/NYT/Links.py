import requests
import time
import os
import config

#start variables
start_year = 2022
# start_year = config.get_input_number("Input Start Year: ")
amount_years = 2
# amount_years = config.get_input_number("Input amount of years: ")

topics = config.topics
API_KEY = config.NYT_API_KEY
for i in range(amount_years):
    year = start_year + i
    month = 0
    for month_idx in range(12):
        month += 1
        if os.path.exists(f"data/NYT/links/{topics[0]}/{year}/month{month}.txt") and os.path.exists(f"data/NYT/links/{topics[1]}/{year}/month{month}.txt"):
            print(f"File 'month{month}.txt'  already exists. Skipping...")
            continue
        URL = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={API_KEY}"
        try:
            #get data
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()
            articles = data.get("response", {}).get("docs", [])
            
        except requests.exceptions.RequestException as e:
            print(f"Fehler beim Abrufen der Daten: {e}")
            time.sleep(5)
        except ValueError:
            print("Fehler beim Parsen der JSON-Antwort.")
        
        
        for topic in topics:
            file_path = f"data/NYT/links/{topic}/{year}/month{month}.txt"
            with open(file_path, "w", encoding="utf-8") as file:
                for article in articles:
                    url = article.get("web_url", "No URL")
                    if f"/{topic}/" in url:
                        if any(format in url for format in ["/interactive/", "/slideshow/", "/video/", "/crossword/"]):
                            continue
                        file.write(url + '\n')
                        
            print(f"Die Links für {topic} wurden erfolgreich in '{year}/month{month}.txt' gespeichert.")
            time.sleep(3)
            
