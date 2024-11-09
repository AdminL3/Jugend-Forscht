import requests
import time

# Load proxies and URLs from files
with open(r'data-collection\proxyrotation\success.txt', 'r') as f:
    proxies = f.read().splitlines()

with open(r'data-collection\proxyrotation\urls.txt', 'r') as f:
    urls = f.read().splitlines()

results = []

# Main loop to rotate proxies
proxy_index = 0
# print(len(urls))
for url in urls:
    proxy = proxies[proxy_index]
    print(f"Using proxy: {proxy} for URL: {url}")

    try:
        # Use requests.get with a proxy
        response = requests.get(
            url, proxies={"http": proxy, "https": proxy}, timeout=10, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})

        with open(r'data-collection\proxyrotation\content.txt', 'a') as f:
            f.write(response.text)
        results.append(response.text)
        print(f"Successfully fetched content from {url} with {proxy}")
        time.sleep(2)

    except:
        print(f"Failed to fetch {url} with proxy {proxy}")
        proxy_index += 1  # Move to the next proxy in case of failure

        # Check if there are any proxies left
        if proxy_index >= len(proxies):
            print("No more proxies available. Exiting.")
            break

# Save the results to a file
if results:
    with open(r'data-collection\proxyrotation\results.txt', 'w') as f:
        f.write('\n'.join(results))
    print("Finished saving results.")
else:
    print("No results to save.")
