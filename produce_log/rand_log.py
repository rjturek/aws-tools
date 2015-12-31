# Generate random log messages for a mythical clients and servers.
import random
import time
import sys

class RandomLogger(object):
    """
        Generate a series of randomly created log records indicating client calling service.
    """
    clients = ('a', 'b', 'c', 'x')
    services = ('b', 'c', 'w', 'x', 'y', 'z')
    out_stream = None

    def __init__(self, out_stream=sys.stdout):
        self.out_stream = out_stream
        print(type(self.out_stream))

    def gen_log_line(self):
        for _ in range(5):
            sleep = random.randint(4, 300)/100
            time.sleep(sleep)
            cli = random.randint(0, len(self.clients) - 1)
            srv = random.randint(0, len(self.clients) - 1)
            yield str("client=%s calling service=%s" % (self.clients[cli], self.services[srv]))

    def gen_log(self):
        for line in self.gen_log_line():
            print("got it", line)
            self.out_stream.write(line + "\n")
            self.out_stream.flush()

if __name__=="__main__":
    rand_logger = RandomLogger(out_stream=sys.stdout)
    rand_logger.gen_log()
