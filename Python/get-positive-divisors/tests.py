import unittest
import main


class Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(main.get_pos_divs(1), [1])

    def test_prime_num(self):
        self.assertEqual(main.get_pos_divs(7), [1, 7])

    def test_perfect_square(self):
        self.assertEqual(main.get_pos_divs(36), [1, 2, 3, 4, 6, 9, 12, 18, 36])

    def test_other_nums(self):
        nums = [25, 42]
        pos_divs = [[1, 5, 25], [1, 2, 3, 6, 7, 14, 21, 42]]

        for num, pos_div in zip(nums, pos_divs):
            self.assertEqual(main.get_pos_divs(num), pos_div)


if __name__ == '__main__':
    unittest.main()
