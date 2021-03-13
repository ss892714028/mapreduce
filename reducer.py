#!/bin/python

import sys
from itertools import groupby
from operator import itemgetter

SEPARATOR = '\t'


def read(std_in):
    for line in std_in:
        yield line.rstrip().split(SEPARATOR, 1)


def main():
    data = read(sys.stdin)
    for curr, group in groupby(data,itemgetter(0)):
        try:
	    total_count = sum(int(count) for curr, count in group)
            print('{}{}{}'.format(curr, SEPARATOR, total_count))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
