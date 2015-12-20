import threading
import requests
import time
from pprint import pprint

from multiprocessing.dummy import Pool as ThreadPool


urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
]

# Make the Pool of workers
pool = ThreadPool(2)

def read_url(url):
    r = requests.get(url)
    print(threading.current_thread(), r)

start = time.time()
# Open the urls in their own threads
# and return the result
f = pool.map(read_url, urls)
pprint(f)

#close the pool and wait for the work to finish
pool.close()
pool.join()
end = time.time()
print(end - start)
