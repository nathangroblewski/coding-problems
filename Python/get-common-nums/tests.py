#!/usr/bin/env python

import main
import unittest


class Tests(unittest.TestCase):
    def test_no_common_nums(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(main.get_common_nums(*nums), [1, 2, 3, 4, 5, 6, 7])

    def test_one_common_num(self):
        nums = [1, 2, 3, 4, 5, 1, 6, 7]
        self.assertEqual(main.get_common_nums(*nums), [1])

    def test_two_common_nums(self):
        nums = [5, 4, 3, 2, 4, 5, 1, 6, 1, 2, 5, 4]
        self.assertEqual(sorted(main.get_common_nums(*nums)), [4, 5])


if __name__ == '__main__':
    unittest.main()
