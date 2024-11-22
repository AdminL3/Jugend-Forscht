import os
import time
import datetime
import requests
import config  # Your API key stored here


def fetch_guardian_links(year, month):
    """
    Fetches article links from The Guardian for a given topic, year, and month.
    Saves links to a text file in the appropriate directory.
    """

    # Define API parameters
    params = {
        "from-date": f"{year}-{month:02}-01",
        "to-date": (datetime.date(year, month, 1) + datetime.timedelta(days=31)).replace(day=1).isoformat(),
        "api-key": GUARDIAN_API_KEY,
        "page-size": 50,  # Maximum results per page
        "page": 1,  # Start from page 1
        "show-fields": "trailText",  # Optional: fetch summary
    }

    all_links = []
    while True:
        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

            # Check if there are results
            results = data.get("response", {}).get("results", [])
            if not results:
                break

            # Collect links from the response
            links = [result["webUrl"] for result in results]
            all_links.extend(links)

            # Pagination: Stop if on the last page
            if not data["response"].get("pages") or params["page"] >= data["response"]["pages"]:
                break

            params["page"] += 1
            time.sleep(1)  # Respect API rate limits

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {year}-{month:02}: {e}")
            time.sleep(7)  # Wait before retrying
            break
    return all_links


# Define your API key
GUARDIAN_API_KEY = config.GUARDIAN_API_KEY

# Define the start year, amount of years, and topics
start_year = 2020
amount_years = 2
topics = ["politics", "world", "opinion"]

# Define the Guardian API base URL
BASE_URL = "https://content.guardianapis.com/search"

# Calculate start and end dates
start_date = datetime.date(start_year, 1, 1)
try:
    end_date = start_date.replace(year=start_date.year + amount_years)
except ValueError:
    end_date = start_date + datetime.timedelta(days=amount_years * 365)


for i in range(amount_years):
    year = start_year + i
    for month in range(1, 13):

        all_links = fetch_guardian_links(year, month)

        for topic in topics:
            file_path = f"data/guardian/links/{
                topic}/{year}/month{month:02}.txt"
            os.makedirs(file_path, exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as file:
                for link in all_links:
                    # if (topic.lower() in link.lower()):
                    file.write(link + "\n")

        print(f"Saved {len(all_links)} links for {
            topic}, {year}-{month:02}.")
