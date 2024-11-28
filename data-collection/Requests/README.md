# Data Collection Script

###### Check out a detailed Description at [The Guardian](../Guardian/)

## Benefits:

- This script works really well with the Guardian
- Easy to set up and use
- Can get really fast results

## Problems:

- You get blocked really quick ([NYT](../NYT/)), so you have to resort to other methods
- Add Error handling for too many Requests

## Requirements

- `requests` library

```sh
pip install requests
```

## Usage

```python
import os
import time
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
```
