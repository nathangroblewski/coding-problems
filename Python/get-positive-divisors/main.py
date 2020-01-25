#!/usr/bin/env python

from math import sqrt
import sys


def get_pos_divs(num):
    """ generates and returns a list of positive divisors up to the given number """
    pos_divs = set()  # use a set to cover case of perfect square

    for i in range(1, int(sqrt(num))+1):
        if num % i == 0:
            pos_divs.add(i)
            pos_divs.add(num // i)

    return sorted(pos_divs)


if __name__ == '__main__':
    print(get_pos_divs(int(sys.argv[1])))
