import requests
from nltk.sentiment import SentimentIntensityAnalyzer
import config

URL = f"https://api.nytimes.com/svc/archive/v1/2024/1.json?api-key={
    config.NYT_API_KEY}"

try:
    # Hardcoding the API key in the request URL
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    articles = data.get("response", {}).get("docs", [])

    # Write results to a file
    with open("articles.txt", "w", encoding="utf-8") as file:
        for article in articles:
            title = article.get("headline", {}).get("main", "No Title")
            abstract = article.get("abstract", "No Abstract")
            url = article.get("web_url", "No URL")
            file.write(f"Title: {title}\n")
            file.write(f"Abstract: {abstract}\n")
            file.write(f"URL: {url}\n")
            file.write("\n" + "="*50 + "\n\n")

    print("Die Artikel wurden erfolgreich in 'articles.txt' gespeichert.")

except requests.exceptions.RequestException as e:
    print(f"Fehler beim Abrufen der Daten: {e}")
except ValueError:
    print("Fehler beim Parsen der JSON-Antwort.")
