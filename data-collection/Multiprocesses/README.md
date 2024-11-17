# Using Threads to Optimize Data Collection Process

### 1. Testing Different pools

```python
import multiprocessing
import time


def sleep(n):
    time.sleep(5-n)
    print(n)


numbers = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        pool.map(sleep, numbers)
```

###### Output:

New output every second

```bash
5
4
3
2
1
```

### 2. Applying to Selenium gathering

1. Setting up the function

```python
def Selenium(n):
    start_year = 2020
    amount_years = 1
    topics = ["world", "politics", "opinion"]
    amount_month = 1
    last_date = 0
    ...
```

2. Setting the start month to **n**

```python
    start_month = n
```

3. Specifying the Month to run

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

4. Running the functions at the same time

```
if **name** == "**main**":
    with multiprocessing.Pool() as pool:
        pool.map(Selenium, numbers)
```
