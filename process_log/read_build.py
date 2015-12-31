import os

print("HHHHHEYYYYY")
print(os.getcwd())

# log = open(os.path.dirname(__file__) + '../data/calls.log','r')
log = open('../data/calls.log','r')

lineslist = log.readlines()

for l in [line.rstrip() for line in lineslist]:
    print(l)
