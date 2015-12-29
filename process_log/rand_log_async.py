# Generate random log messages for a mythical clients and servers.
import asyncio
import random
import time
import sys

"""
    Generate a series of randomly created log records indicating client calling service.
"""
clients = ['a', 'b', 'c', 'x']
services = ['b', 'c', 'w', 'x', 'y', 'z']
out_stream = None

async def gen_log_line():
    for _ in range(2000):
        sleep = random.randint(4, 300)/100
        await asyncio.sleep(sleep)

        cli_idx = random.randint(0, len(clients) - 1)
        cli = clients[cli_idx]

        tmp_svcs = list(services)
        if cli in services:
            tmp_svcs.remove(cli)

        svc_idx = random.randint(0, len(tmp_svcs) - 1)
        svc = tmp_svcs[svc_idx]

        if cli == svc:
            raise Exception(cli + svc)

        return str("client=%s service=%s time=%s" % (cli, svc, str(sleep)))

async def main():
    while True:
        print(await gen_log_line())


if __name__=="__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())