import unittest

"""
Task 5:
Create a fully functional dictionary just out of functions
"""


pairs = [("n", "never"), ("c", "code"), ("a", "alone")]


class Testsuite(unittest.TestCase):
    result = dict(pairs)

    def test(self):
        self.assertEqual(self.result["n"], get("n"))
        self.assertEqual(self.result["c"], get("c"))
        self.assertEqual(self.result["a"], get("a"))


def get(key):
    return store(pairs)(key)


def store(items):
    def pair((key, value)):
        return lambda k: value if k == key else None

    def merge(acc, el):
        return lambda k: acc(k) or el(k)

    return reduce(merge, map(pair, items))