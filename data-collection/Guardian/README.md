# Data Collection from "The Guardian"

## Step 1: Get Links from **Guardian API**

This step involves collecting article links from the New York Times (NYT) API. You can find the code for this step in the [`Links.py`](Links.py) file.

#### 1. **Get NYT API Key**:

- Create a developer account on the [NYT Developer Portal](https://open-platform.theguardian.com/).
- Register for an API key.
- You will receive it via email.
- I recommend using [Temp Mail](https://temp-mail.org/en/) to generate multiple at once.

#### 2. **Use API**:

- Go to the [Guardian Documentation](https://open-platform.theguardian.com/documentation/) page.
- Explore the API structure.

- Example Request with tag "environment/recycling":

```python
URL = "https://content.guardianapis.com/search?tag=environment/recycling&api-key=test"
response = requests.get(BASE_URL, params=params)
```

#### 3. Parse json

- Now we get a long json string, where we have to extract the url
- Choose the data you want to collect (links or titles).

```python
links = [result["webUrl"] for result in results]
```

---

## Step 2: Sort Links by Category

- Lets remove the articles you dont want
- And sort them in the correct categories
- See [`Parse_Links.py`](./Parse_Links.py)

```python
if any(format in url for format in ["/interactive/", "/slideshow/", "/video/", "/crossword/"]):
```

- Save the data as a new file in the correct folder.

```python
file.write(link + "\n")
```

---

## Step 3: Extract Source Code from URLs

In this step, you can choose from different methods to extract the source code from URLs.

###### The option I used:

### Requests

1. **Install** Requests:

   - If not already done

   ```sh
   pip install requests
   ```

2. Use **Requests**:

   - Access HTML Code

   ```python
   response = requests.get(url)
   page_source = response.text
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
