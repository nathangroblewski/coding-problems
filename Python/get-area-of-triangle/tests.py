#!/usr/bin/env python

import main
import unittest


class Tests(unittest.TestCase):
    def test_area_of_triangle(self):
        self.assertEqual(main.get_area_of_triangle(3, 4, 5), 6.0)

    def test_negative_number_rejected(self):
        self.assertRaises(main.InvalidTriangleException,
                          main.get_area_of_triangle, 1, 11, -4)

    def test_invalid_triangle_dimensions_rejected(self):
        self.assertRaises(main.InvalidTriangleException,
                          main.get_area_of_triangle, 1, 10, 12)

if __name__ == '__main__':
    unittest.main()


