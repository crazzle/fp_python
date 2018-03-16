from collections import namedtuple
import unittest

"""
Functional Statemachine:
Build a small power generator.
The generator generates per Default 0kw.
You can give it a target that it approaches over time.
"""

'''
Helper function
'''
def foldLeft(f, acc, items):
    if not items:
        return acc
    else:
        head, tail = items[0], items[1:]
        return foldLeft(f, f(head, acc), tail)

'''
States
'''
Generator = namedtuple("Generator", ["output", "state"])
Running = namedtuple("Running", [])
Dispatching = namedtuple("Dispatching", [])

'''
State-Transition

Signature:
target, generator -> (Int, State), Generator
'''
def action(target, generator):
    from operator import add, sub
    output, state = generator
    if target == output:
        return (output, state), Generator(target, Running())
    if target < output:
        return (output, state), Generator(sub(output, 1), Dispatching())
    if target > output:
        return (output, state), Generator(add(output, 1), Dispatching())


class Testsuite(unittest.TestCase):
    replay = "4+4+4+3+3+3+3+5+5+5+5+5+1+1+1+1+1+1"
    ergebnis = Generator(output=1, state=Running())

    def test_statemachine(self):
        self.fail("Not implemented yet")
