import threading
import time
import itertools

from random import randint

print("waaaaaaaaa")

def yield_waits():
    for _ in range(10):
        yield randint(0,30)

def func1(generator):
    for wait in generator:
        time.sleep(wait/10)
        print(threading.current_thread(), "func1", wait)

def func2(generator):
    for wait in generator:
        time.sleep(wait/10)
        print(threading.current_thread(), "func2", wait)

t1 = threading.Thread(target=func1, args=(yield_waits()))
t2 = threading.Thread(target=func2, args=(yield_waits()))

t1.start()
t2.start()
