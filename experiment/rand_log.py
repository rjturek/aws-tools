# Generate random log messages for a mythical clients and servers.
import logging
import random
import time
clients = ('a', 'b', 'c', 'x')
services = ('b', 'c', 'w', 'x', 'y', 'z')

def gen_log_line():
    for _ in range(300):
        sleep = random.randint(4, 300)/100
        time.sleep(sleep)
        cli = random.randint(0, len(clients) - 1)
        srv = random.randint(0, len(clients) - 1)
        yield str("client=%s calling service=%s" % (clients[cli], services[srv]))

def gen_log():
    for line in gen_log_line():
        logging.debug(line)

def initialize_log():
    logging.basicConfig(level=logging.DEBUG)

def main():
    initialize_log()
    gen_log()

if __name__=="__main__":
    main()
