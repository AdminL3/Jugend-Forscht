# Data Collection from the NYT

---

## Step 1: Get Links from **NYT API**

This step involves collecting article links from the New York Times (NYT) API. You can find the code for this step in the [Get_Links.py](https://github.com/AdminL3/Jugend-Forscht/blob/main/data-collection/Get_Links.py) file.

1. **Get NYT API Key**:

   - Create a developer account on the [NYT Developer Portal](https://developer.nytimes.com/).
   - Go to the [NYT Apps](https://developer.nytimes.com/my-apps) page.
   - Get your API key.

2. **Use API**:

   - Go to the [NYT APIs](https://developer.nytimes.com/apis) page.
   - Explore the API structure.
   - Choose the data you want to collect (links or titles).
   - Save the data as a file.

---

## Step 2: Extract Source Code from URLs

In this step, you can choose from different methods to extract the source code from URLs. Here are the options:

### 1. Selenium

1. **Install** Selenium:

   ```bash
   pip install selenium
   ```

2. Use **Selenium**:

   - Create Options

   ```bash
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")
   options.add_argument("--disable-search-engine-choice-screen")
   options.add_experimental_option("detach", True)
   options.add_argument("--headless")
   driver = webdriver.Chrome(options=options)
   ```

   - Create Driver

   ```bash
   driver = webdriver.Chrome(options=options)
   ```

   - Access Content

   ```bash
   while True:
      try:
         driver.get(url)
         page_source = driver.execute_script(
               "return document.documentElement.outerHTML;")
         break
      except:
         print("Error")
   ```

### 2. Requests

- This Works for some time until you get blocked. Then you should use Proxys or External APIs --> See [**Proxyrotation**](#4-proxyrotation) and [**ExternalAPIs**](#3-external-api)

1. **Install** Requests:

   ```bash
   pip install requests
   ```

2. Use **Requests**:

   - Access HTML Code

   ```bash
   response = requests.get(url)
   page_source = response.text
   ```

### 3. External API

- I am using [ScraperAPI](https://www.scraperapi.com/)
- This Works, but you are limited tokens and its slower

1. **Install** Requests:

   ```bash
   pip install requests
   ```

2. Access **API**:

   ```bash
   payload = {'api_key': api_key,
               'url': url}
   r = requests.get('https://api.scraperapi.com/', params=payload)
   ```

### 4. Proxyrotation

- You can get free Proxys at [Free Proxy List](https://free-proxy-list.net/)
- Some Proxys do not work!

1. **Install** Requests:

   ```bash
   pip install requests
   ```

2. Check which Proxies work:

   - Download Proxies
   - Loop through them and save the working ones as a file

3. Use working proxies to access HTML
   - See [**2. Requests**](#2-requests)

---

## Step 2.5: Use AWS to run Python in the cloud

- See my Subfolder [Run Python in the Cloud](./AWS/)

- Run your scripts in the Cloud to reduce computer usage

---

## Step 3: Convert HTML to Text

#### 1. Use **BeautifulSoup** to Parse HTML:

- Usually I would just use Beautiful Soup to parse HTML

1. **Install** Requests:

   ```bash
   pip install requests beautifulsoup4
   ```

   ```bash
   import requests
   from bs4 import BeautifulSoup
   ```

1. **Use** BS4:

- This totally depends on your HTML Code

  ```bash
  response = requests.get(url)
  ```

  ```bash
  soup = BeautifulSoup(response.text, 'html.parser')
  ```

  ```bash
  text = soup.get_text(separator='\n', strip=True)
  ```

#### 2. Use **Re** to Parse HTML:

- But Since NYT really tries to prevent me from getting their data
- I had to use RE to parse the data from some javascript encoding

  ```bash
  import re
  ```

  ```bash
  def get_text_from_html(html):
    matches = re.findall(r'"text":"(.*?)"', html)

    matches = list(dict.fromkeys(matches))

    text = ""
    for match in matches:
        text += match + "\n"

    return text
  ```

---

## 3. Extra Functionality

1. **Find empty files**:

   - Sometimes the content wasnt downloaded correcly so i checked where there where empty files without content.

     ```bash
     for dirpath, dirnames, filenames in os.walk(base, topdown=False):
        # Check if the directory is empty
        if not os.listdir(dirpath):  # If the folder is empty
              print(f"Deleting empty folder: {dirpath}")
              os.rmdir(dirpath)  # Delete the empty folder

        # Also check for empty files and delete them
        for file in filenames:
              file_path = os.path.join(dirpath, file)
              if os.path.getsize(file_path) == 0:  # If the file is empty
                 print(f"Deleting empty file: {file_path}")
                 os.remove(file_path)
     ```

   - Again, this depends on your folder structure.

2. **Find missing files**:

   - To check what files are missing i used a simple script
   - See _file_checker.py_

---

## Result

- This is only a part of the full project!

- The part, where we extract the full NYT Source Code

- View the whole Projekt at [Github](https://github.com/AdminL3/Jugend-Forscht/)
