import unittest

"""
Task 3:
Sum up a list of numbers

Example:
[78, 67, 65] = 210

"""


class Testsuite(unittest.TestCase):

    numbers = [78, 101, 118, 101, 114, 32, 67, 111, 100, 101, 32, 65, 108, 111, 110, 101]
    result = 1450

    def test(self):
        self.assertEqual(self.result, sum_up(self.numbers))


def sum_up(numbers):
    pass


