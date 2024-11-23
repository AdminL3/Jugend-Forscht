# Data Collection from the New York Times

## Step 1: Get Links from **Guradian API**

This step involves collecting article links from the New York Times (NYT) API. You can find the code for this step in the [`Links.py`](Links.py) file.

1. **Get NYT API Key**:

   - Create a developer account on the [NYT Developer Portal](https://open-platform.theguardian.com/).
   - Register for an API key.
   - You will receive it via email.

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

###### The option I used:

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

###### Error in Selenium:

![Captcha Test Selenium](../Errors/Error%201.png)

###### Even in headless browser:

As HMTL:
![Captcha Test Headless Selenium](../Errors/Error%206.png)

## Other Options:

### 2. Requests

- This Works for some time until you get blocked. Then you should use Proxys or External APIs --> See [**Proxyrotation**](#4-proxyrotation) and [**ExternalAPIs**](#3-external-api)

1. **Install** Requests:

   ```sh
   pip install requests
   ```

2. Use **Requests**:

   - Access HTML Code

   ```python
   response = requests.get(url)
   page_source = response.text
   ```

   The Error:

   - Result of Data was a captcha
     ![Requests Error](../Errors/Error%205.png)

### 3. External API

- I am using [ScraperAPI](https://www.scraperapi.com/)
- This Works, but you have limited tokens and its slower

1. **Install** Requests:

   ```sh
   pip install requests
   ```

2. Access **API**:

   ```python
   payload = {'api_key': api_key,
               'url': url}
   r = requests.get('https://api.scraperapi.com/', params=payload)
   ```

### 4. Proxyrotation

- You can get free Proxys at [Free Proxy List](https://free-proxy-list.net/)
- Some Proxys do not work!

1. **Install** Requests:

   ```sh
   pip install requests
   ```

2. Check which Proxies work:

   - Download Proxies
   - Loop through them and save the working ones as a file

3. Use working proxies to access HTML

   - See [**2. Requests**](#2-requests)

###### Free Proxies are unfortunately very unreliable

### 5. Other Errors i had to deal with

#### Another Blocker on Selenium:

![Requests Error](../Errors/Error%202.png)

---

#### And countless paywalls:

1.  ![Paywall Error 1](../Errors/Error%203.png)

---

2.  ![Paywall Error 2](../Errors/Error%204.png)

---

3. <img src="../Errors/Error%206.jpg" alt="Login Wall" width="300"/>

---
