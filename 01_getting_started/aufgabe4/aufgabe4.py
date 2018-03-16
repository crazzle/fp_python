import unittest

"""
Task 4:
Parse the term and sum up the numbers

Detail:
We now know Higher-Order-Functions and implemented our own reduce.
Use "reduce" now to sum up the numbers in the string.

Signature of reduce:
def reduce(f, sequence, initial=None)

Example:
"78+67+65" = 210
"""

class Testsuite(unittest.TestCase):

    numbers = "78+101+118+101+114+32+67+111+100+101+32+65+108+111+110+101"
    problem = "++78+101+118+101+114+32+67++111+100+101+32+65+108+111++++110+101"
    result = 1450

    def test(self):
        self.assertEqual(self.result, fold(self.numbers))
        self.assertEqual(self.result, fold(self.problem))


def fold(numbers):
    pass