#!/usr/bin/env python

import ast
from collections import Counter
from six import iteritems
import sys


def get_common_nums(*nums):
    """ returns a list of the most frequently occurring integers in a list """
    count_map = Counter(nums)
    max_count = max(count_map.values())

    return [num for num, count in iteritems(count_map) if count == max_count]


if __name__ == '__main__':
    print(get_common_nums(*[i for i in map(int, sys.argv[1:])]))
