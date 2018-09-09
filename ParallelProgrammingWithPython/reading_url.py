import urllib.request
from multiprocessing.pool import ThreadPool as Pool
import sys
import multiprocessing
import subprocess
from concurrent.futures import ThreadPoolExecutor

sites = [
    'https://www.yahoo.com/',
    'http://www.cnn.com',
    'http://www.python.org',
    'http://www.jython.org',
    'http://www.pypy.org',
    'http://www.perl.org',
    'http://www.cisco.com',
    'http://www.facebook.com',
    'http://www.twitter.com',
    'http://www.macrumors.com/',
    'http://arstechnica.com/',
    'http://www.reuters.com/',
    'http://abcnews.go.com/',
    'http://www.cnbc.com/',
    'http://www.cnbc.com/',
]


def sitesize(url):
    """Determine the size of a websitee"""
    with urllib.request.urlopen(url) as u:
        page = u.read()
        return url, len(page)


pool = Pool(10)
for result in pool.imap_unordered(sitesize, sites):
    print(result)


def run(arg):
    print("starting %s" % arg)
    p = multiprocessing.Process(target=print, args=("running", arg))
    p.start()
    p.join()
    print("finished %s" % arg)


if __name__ == "__main__":
    n = 16
    tests = range(n)
    with ThreadPoolExecutor(n) as pool:
        for r in pool.map(run, tests):
            pass
