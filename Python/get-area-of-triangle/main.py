#!/usr/bin/env python

from math import sqrt
import sys
from typing import List

def test(num: int) -> List[int]:
    return num + 1



def get_area_of_triangle(s1, s2, s3):
    """ Uses Heron's formula to calculate the area of a triangle """

    if is_valid_triangle(s1, s2, s3) and valid_lengths(s1, s2, s3):
        s = 0.5 * (s1 + s2 + s3)  # semi-perimeter of the triangle
        area = sqrt(s * (s - s1) * (s - s2) * (s - s3))
        return round(area, 2)
    else:
        raise InvalidTriangleException('Invalid lengths provided')


def valid_lengths(s1, s2, s3):
    """ returns true if all sides of the triangle are positive """
    return s1 > 0 and s2 > 0 and s3 > 0


def is_valid_triangle(s1, s2, s3):
    """ returns true if it's a valid triangle """
    return s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1


class InvalidTriangleException(Exception):
    pass


if __name__ == '__main__':
    print(get_area_of_triangle(*[i for i in map(int, sys.argv[1:])]))
