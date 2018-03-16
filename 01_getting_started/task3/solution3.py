import unittest
from operator import add

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
        self.assertEqual(self.result, foldRight(add, 0, self.numbers))
        self.assertEqual(self.result, foldLeft(add, 0, self.numbers))
        self.assertEqual(self.result, sum(self.numbers))


def sum_up(zahlen):
    summe = 0
    for zahl in zahlen:
        summe+=zahl
    return summe


def foldRight(f, acc, items):
    if not items:
        return acc
    else:
        head, tail = items[0], items[1:]
        return f(foldRight(f, acc, tail), head)


def foldLeft(f, acc, items):
    if not items:
        return acc
    else:
        head, tail = items[0], items[1:]
        return foldLeft(f, f(acc, head), tail)
