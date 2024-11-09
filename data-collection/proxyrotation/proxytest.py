import requests
import time

with open(r'data-collection\proxyrotation\success.txt', 'r') as f:
    proxies = f.read().splitlines()


url = r'https://books.toscrape.com/'


def fetch_with_proxy(url, proxy):
    try:
        # Raise an exception for HTTP error responses
        response = requests.get(

            # Return the content of the response
            url, proxies={"http": proxy, "https": proxy}, timeout=10)
        response.raise_for_status()
        # Print an error message if the request fails
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url} with proxy {proxy}: {e}")
        return None


success = []
for proxy in proxies:
    html_content = fetch_with_proxy(url, proxy)

    if html_content:
        print(f"Fetched content from {url} with {proxy}")
        print(html_content)
        time.sleep(2)
        success.append(proxy)
    else:
        print(f"Failed to fetch content from {url}")

with open(r'data-collection\proxyrotation\success.txt', 'w') as f:
    f.write('\n'.join(success))

print("Finished saving:")
