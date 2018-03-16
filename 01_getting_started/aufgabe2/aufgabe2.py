import unittest

"""
Task 2:
Convert the string of numbers to a list of integers

Example:
"78+67+65" = [78, 67, 65]
"""


class Testsuite(unittest.TestCase):
    numbers = "78+101+118+101+114+32+67+111+100+101+32+65+108+111+110+101"
    result = [78, 101, 118, 101, 114, 32, 67, 111, 100, 101, 32, 65, 108, 111, 110, 101]

    def test(self):
        assert convert(self.numbers) == self.result


def convert(numbers):
    pass







