#!/bin/python


import sys

SEPARATOR = '\t'


def read_input(std_input):
    for line in std_input:
        yield line.strip()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        print('{}{}{}'.format(words, separator, 1))

if __name__ == "__main__":
    main()

