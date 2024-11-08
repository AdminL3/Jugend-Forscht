import requests


urls = ["https://www.nytimes.com/2020/01/01/world/asia/hong-kong-protest.html",
        "https://www.nytimes.com/2020/01/01/world/middleeast/iraq-embassy-iran.html",
        "https://www.nytimes.com/2020/01/01/world/australia/fires.html",
        "https://www.nytimes.com/2020/01/01/world/middleeast/us-embassy-baghdad-iraq.html",
        "https://www.nytimes.com/2020/01/01/world/canada/pokemon-go-canada-military.html",
        "https://www.nytimes.com/2020/01/01/world/asia/north-korea-kim-trump.html",
        "https://www.nytimes.com/2020/01/01/world/americas/mexico-prison-fight.html",
        "https://www.nytimes.com/2020/01/01/world/middleeast/israel-netanyahu-immunity.html"]


for i in range(len(urls)):
    payload = {'api_key': '18c0782353baecd44be6ba1f1cb08eaa',
               'url': urls[i]
               }
    r = requests.get('https://api.scraperapi.com/', params=payload)
    with open(f"test/get/{i}.txt", "w", encoding="utf-8") as f:
        f.write(r.text)
