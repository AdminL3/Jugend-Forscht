import multiprocessing
import time


def sleep(n):
    time.sleep(5-n)
    print(n)


numbers = [1, 2, 3, 4, 5]

with multiprocessing.Pool() as pool:
    pool.map(sleep, numbers)
