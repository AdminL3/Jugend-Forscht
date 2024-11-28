# Data Collection with Scraperapi

- This script uses the `requests` library to fetch the source code of web pages
- It uses the Scraperapi API to avoid getting blocked

---

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

---

- This is a consistent way to access HTML content.
- It is slower than other methods.
- You have limited tokens.
