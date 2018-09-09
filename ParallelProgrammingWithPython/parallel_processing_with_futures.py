import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from random import random
from time import sleep
import urllib.request
import requests
import math

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/'
        ]

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    100
]


def load_url(url):
    with requests.get(url) as conn:
        return conn.text


with concurrent.futures.ThreadPoolExecutor(5) as executor:
    future_to_url = {executor.submit(load_url, url): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print("%r generated an exception: %s" % (url, exc))
        else:
            print("%r page is %d bytes" % (url, len(data)))


def is_prime(number):
    if number % 2 == 0:
        return False
    sqrt_n = math.floor(math.sqrt(number))
    for i in range(3, sqrt_n + 1, 2):
        if i % 2 == 0:
            return False
        else:
            return True


def con_is_prime():
    with concurrent.futures.ProcessPoolExecutor(4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print("%d in prime of %s" % (number, prime))


def return_after_5_sec(num):
    sleep(random.randint(1, 5))
    return "Return of {}".format(num)


pool = ThreadPoolExecutor(5)
futures = []
for x in range(5):
    futures.append(pool.submit(return_after_5_sec, x))
print(wait(futures))

if __name__ == "__main__":
    con_is_prime()
    # load_url(URLS)
