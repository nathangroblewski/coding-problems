import unittest
import main


class Tests(unittest.TestCase):
    def test_is_none(self):
        self.assertTrue(main.is_none_or_empty(None))

    def test_is_empty(self):
        self.assertTrue(main.is_none_or_empty(''))

    def test_not_none_or_empty(self):
        strings = ('a', 'None')
        for s in strings:
            self.assertFalse(main.is_none_or_empty(s))


if __name__ == '__main__':
    unittest.main()
