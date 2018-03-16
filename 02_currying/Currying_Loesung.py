import unittest

"""
Function Currying:
Build a decorator named 'curried' that partially applies
a decorated function and therefore returns a new function.

<Function>.__code__.co_argcount returns the count of parameters
of a function
"""


def curried(func):
    def curry(*args):
        if len(args) == func.__code__.co_argcount:
            ans = func(*args)
            return ans
        else:
            return lambda x: curry(*(args+(x,)))

    return curry

@curried
def test(a, b, c):
    return a+b+c

class Testsuite(unittest.TestCase):
    result = 6

    def test(self):
        test1 = test(1)
        test2 = test1(2)
        self.assertEqual(self.result, test2(3))
