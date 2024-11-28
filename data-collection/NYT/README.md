# Data Collection from the New York Times

## Step 1: Get Links from **NYT API**

This step involves collecting article links from the New York Times (NYT) API. You can find the code for this step in the [`Get_Links.py`](./Get_Links.py) file.

1. **Get NYT API Key**:

   - Create a developer account on the [NYT Developer Portal](https://developer.nytimes.com/).
   - Go to the [NYT Apps](https://developer.nytimes.com/my-apps) page.
   - Get your API key.

2. **Use API**:

   - Go to the [NYT APIs](https://developer.nytimes.com/apis) page.
   - Explore the API structure.

   * Example Request

```python
URL = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={API_KEY}"
```

3. Parse json

- Now we get a long json string, where we have to extract the url
- Choose the data you want to collect (links or titles).

```python
url = article.get("web_url", "No URL")
```

- And remove the articles you dont want

```python
if any(format in url for format in ["/interactive/", "/slideshow/", "/video/", "/crossword/"]):
```

- Save the data as a file.

```python
file.write(url + '\n')
```

---

## Step 2: Extract Source Code from URLs

In this step, you can choose from different methods to extract the source code from URLs.

- This is a very tedious process, as NYT tries to prevent you from getting their data
- [Here](../Errors/) are the Errors i encountered
- I tried multiple methods, but they all got blocked after some time

###### The option that worked in the end:

### Selenium

1. **Install** Selenium:

   ```sh
   pip install selenium
   ```

2. Use **Selenium**:

   - Create Options

   ```python
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")
   options.add_argument("--disable-search-engine-choice-screen")
   options.add_experimental_option("detach", True)
   options.add_argument("--headless")
   driver = webdriver.Chrome(options=options)
   ```

   - Create Driver

   ```python
   driver = webdriver.Chrome(options=options)
   ```

   - Access Content

   ```python
   while True:
      try:
         driver.get(url)
         page_source = driver.execute_script(
               "return document.documentElement.outerHTML;")
         break
      except:
         print("Error")
   ```

---

## Other Options to get Source Code:

### 1. Requests

- This worked well with [The Guardian](../The%20Guardian/).
- More Documentation for Requests can be found [here](../Requests/)
- For the [NYT](../NYT/), this works for some time until you get blocked.

### 2. External API

###### [ScraperAPI](../Scraperapi/)

- This Works, but you have limited tokens and its slower
- Check my Docs out [here](../Scraperapi/)
- And their website [here](https://www.scraperapi.com/)

### 3. Proxyrotation

- Rotate Proxys to avoid getting blocked
- More Documentation can be found [here](../Proxyrotation/)
- Free Proxies are unfortunately very unreliable

---

## Step 3: Convert HTML to Text

- Usually I would just use Beautiful Soup to parse HTML
- See [The Guardian](../The%20Guardian/) for more information

- But Since NYT really tries to prevent me from getting their data
- I had to use RE to parse the data from some javascript encoding

- File: [`Extract_Text.py`](./Extract_Text.py)

  ```python
  import re
  ```

  ```python
  def get_text_from_html(html):
    matches = re.findall(r'"text":"(.*?)"', html)

    matches = list(dict.fromkeys(matches))

    text = ""
    for match in matches:
        text += match + "\n"

    return text
  ```

---
