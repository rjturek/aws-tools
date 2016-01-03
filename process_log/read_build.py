from pprint import pprint
from decimal import *
from collections import defaultdict
from collections import namedtuple
# ServiceCalls = namedtuple('ServiceCalls', ['service', 'count', 'avgtime'])

getcontext().prec = 4


def create_svc_dict():
    print("Creating svc dict")
    return {}

def create_svcs_dict():
    print("Creating svcs dict...")
    # Named tuple essentially a class with member variables
    return defaultdict(create_svc_dict)

graph = defaultdict(create_svcs_dict)

log = open('../data/calls.log','r')

lineslist = log.readlines()

for l in [line.rstrip() for line in lineslist]:
    # print(l)
    elems = l.split()
    cli = elems[0].split('=')[1]
    svc = elems[1].split('=')[1]
    tim = elems[2].split('=')[1]
    # print(cli, svc, tim)
    if not graph[cli][svc]:
        graph[cli][svc]['name'] = svc
        graph[cli][svc]['count'] = 0
        graph[cli][svc]['avgtime'] = Decimal(0.000)

    graph[cli][svc]['count'] += 1
    tmp_time = Decimal((graph[cli][svc]['avgtime'] * (graph[cli][svc]['count'] - 1) + Decimal(tim)) / graph[cli][svc]['count'])
    graph[cli][svc]['avgtime'] = tmp_time
    # graph[cli][svc]['avgtime'] += Decimal(tim)

pprint(graph)
