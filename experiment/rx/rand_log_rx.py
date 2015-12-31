# Generate random log messages for a mythical clients and servers.
# import site
# print(site.getsitepackages())
#
# import distutils.sysconfig
# print(distutils.sysconfig.get_python_lib())
#
# import os
# for k in os.environ:
#     print(k, os.environ[k])

import rx
print(rx)
from rx import Observer
from rx import Observable

print(Observer)
print(Observable)



import random
import time
"""
    Generate a series of randomly created log records indicating client calling service.
"""
clients = ['a', 'b', 'c', 'x']
services = ['b', 'c', 'w', 'x', 'y', 'z']
out_stream = None

class random_logger_observable(Observer):

    def on_next(self, x):
        return self._gen_log_record(self)

    def on_error(self, e):
        print("Got error: %s" % e)

    def on_completed(self):
        print("Sequence completed")

    def _gen_log_record(self, x):
        sleep = random.randint(4, 400)/1000
        time.sleep(sleep)

        cli_idx = random.randint(0, len(clients) - 1)
        cli = clients[cli_idx]

        tmp_svcs = list(services)
        if cli in services:
            tmp_svcs.remove(cli)

        svc_idx = random.randint(0, len(tmp_svcs) - 1)
        svc = tmp_svcs[svc_idx]

        if cli == svc:
            raise Exception(cli + svc)

        print("client=%s service=%s time=%s" % (cli, svc, str(sleep)))

class something(Observer):

    def on_next(self, x):
        time.sleep(.2)
        print("blah")

    def on_error(self, e):
        print("Got error: %s" % e)

    def on_completed(self):
        print("Sequence completed")


def handleLine(it):
    print(it)

if __name__=="__main__":

    xs = Observable.from_iterable(range(60))
    xs.subscribe(random_logger_observable())

    # xs2 = Observable.from_iterable(range(8))
    # d2 =  xs2.subscribe(something())
