#!bin/python

import sys
from itertools import groupby

SEPARATOR = '\t'


def read(std_in):
    for line in std_in:
        yield line.strip().split(SEPARATOR, 1)


def main():
    data = read(sys.stdin)
    for curr, group in groupby(data):
        try:
            total_count = 0
            for curr, count in group:
                total_count += count
            print('{}{}{}'.format(curr, SEPARATOR, total_count))
        except ValueError:
            pass

