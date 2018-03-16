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
        self.assertListEqual(self.result, convert(self.numbers.split("+")))
        self.assertListEqual(self.result, convert2(self.numbers.split("+")))
        self.assertListEqual(self.result, map(int, self.numbers.split("+")))


def convert(zahlen):
    def custom_map(f, list):
        if len(list) > 1:
            c = [f(list[0])]
            l = c + custom_map(f, list[1:])
            return l
        return [f(list[0])]
    return custom_map(int, zahlen)


def convert2(zahlen):
    return [int(l) for l in zahlen]