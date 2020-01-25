#!/usr/bin/env python

import sys


def is_none_or_empty(string):
    """ if string is empty or None, returns True - otherwise returns false """
    return not string


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    print(is_none_or_empty(arg))
