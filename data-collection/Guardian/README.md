# Data Collection from "The Guardian" 💂

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
if titles[t].lower() == parts[4]:
   ...
```

- Save the data as a new file in the correct folder.

```python
file.write(link + "\n")
```

---

## Step 3: Extract Source Code from URLs

- In comparison to the NYT, getting the Source Code was a lot easier.
  -The option I used:

### Requests

- See [`Requests.py`](./Requests.py)

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

## Extract Text from Source Code

- Now we have the source code, we can extract the text.
- I used the **BeautifulSoup** library for this task.

#### 1. **Install** Requests and BeautifulSoup:

```sh
pip install requests beautifulsoup4
```

```sh
import requests
from bs4 import BeautifulSoup
```

#### 2. **Use** BS4:

- This totally depends on your HTML Code

```python
soup = BeautifulSoup(html, 'html.parser')
try:
   target_div = soup.find('div', id="maincontent")
   paragraphs = target_div.find_all('p')
except:
   text_content = ""
text_content = soup.title.get_text() + "\n"
for p in paragraphs:
   text_content += p.get_text() + "\n"
```
