#!bin/python

import sys


def read(std_input):
    for line in std_input:
        yield line.strip()


if __name__ == "__main__":
    url = read(sys.stdin)
    print('{}\t{}'.format(url, 1))