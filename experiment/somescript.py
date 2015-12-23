#! /Users/rjt/anaconda/bin/python

print('hey')

fo = open('read_write.py')
lineslist = fo.readlines()
for line in lineslist:
    print(line, end="")
