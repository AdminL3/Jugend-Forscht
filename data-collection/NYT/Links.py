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
        
        for topic in topics:
            file_path = f"data/NYT/links/{topic}/month{month}.txt"
            
            
            with open(file_path, "w", encoding="utf-8") as file:
                for article in articles:
                    url = article.get("web_url", "No URL")
                    if f"/{topic}/" in url:
                        if any(format in url for format in ["/interactive/", "/slideshow/", "/video/", "/crossword/"]):
                            continue
                        file.write(url + '\n')
                        
            print(f"Die Links für {topic} wurden erfolgreich in 'month{month}.txt' gespeichert.")

        time.sleep(3)

    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Daten: {e}")
        time.sleep(5)
    except ValueError:
        print("Fehler beim Parsen der JSON-Antwort.")