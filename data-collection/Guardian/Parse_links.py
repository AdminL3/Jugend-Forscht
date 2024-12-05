import os

start_year = 2010
amount_years = 1
start_month = 1
amount_months = 12
topics = ["politics", "world", "opinion"]
titles = ["Politics", "World", "commentisfree"]
for i in range(amount_years):
    year = start_year + i
    for j in range(amount_months):
        month = start_month + j
        for t, topic in enumerate(topics):
            counter = 0

            file_path = f"data/guardian/links/all/{year}/"
            file_name = f"month{month:02}.txt"
            if os.path.exists(file_path + file_name):
                with open(file_path + file_name, "r", encoding="utf-8") as file:
                    all_links = file.read().splitlines()
                os.makedirs(file_path.replace("all", topic), exist_ok=True)
                with open(file_path.replace("all", topic) + file_name, "w", encoding="utf-8") as file:
                    for link in all_links:
                        if (titles[t].lower() in link.lower()):
                            parts = link.split("/")
                            if titles[t].lower() == parts[3] or titles[t].lower() == parts[4]:
                                file.write(link + "\n")
                                counter += 1

                print(f"Saved {counter} links for {topic}, {year}-{month:02}.")
