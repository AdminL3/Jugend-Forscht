import os

start_year = 2020
amount_years = 2
topics = ["politics", "world", "opinion"]
titles = ["Politics", "World", "commentisfree"]
for i in range(amount_years):
    year = start_year + i
    for month in range(1, 13):
        for t, topic in enumerate(topics):
            counter = 0

            file_path = f"data/guardian/links/all/{year}/"
            file_name = f"month{month:02}.txt"
            if os.path.exists(file_path + file_name):
                with open(file_path + file_name, "r", encoding="utf-8") as file:
                    all_links = file.splitlines()
                with open(file_path.replace("all", topic) + file_name, "w", encoding="utf-8") as file:
                    for link in all_links:
                        if (titles[t].lower() in link.lower()):
                            file.write(link + "\n")
                            counter += 1

                print(f"Saved {counter} links for {topic}, {year}-{month:02}.")
