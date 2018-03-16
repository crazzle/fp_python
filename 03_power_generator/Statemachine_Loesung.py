import unittest
from collections import namedtuple
from operator import add, sub

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
    output, state = generator
    if target == output:
        return (output, state), Generator(target, Running())
    elif target < output:
        return (output, state), Generator(sub(output, 1), Dispatching())
    elif target > output:
        return (output, state), Generator(add(output, 1), Dispatching())


class Testsuite(unittest.TestCase):
    replay = "4+4+4+3+3+3+3+5+5+5+5+5+1+1+1+1+1+1"
    ergebnis = Generator(output=1, state=Running())

    def test_fold(self):
        unit = Generator(0, Running())
        unit = foldLeft(lambda acc, el: action(acc, el)[1], unit, map(int, self.replay.split('+')))
        self.assertEqual(self.ergebnis, unit)

    def test_state_machine(self):
        powerunit = Generator(0, Running())
        _, powerunit = action(5, powerunit)
        _, powerunit = action(5, powerunit)
        _, powerunit = action(5, powerunit)
        _, powerunit = action(5, powerunit)
        _, powerunit = action(5, powerunit)
        _, powerunit = action(5, powerunit)
        self.assertEqual(Generator(5, Running()), powerunit)

        _, powerunit = action(3, powerunit)
        _, powerunit = action(3, powerunit)
        _, powerunit = action(3, powerunit)
        self.assertEqual(Generator(3, Running()), powerunit)

        _, powerunit = action(0, powerunit)
        _, powerunit = action(0, powerunit)
        _, powerunit = action(0, powerunit)
        _, powerunit = action(1, powerunit)
        _, powerunit = action(1, powerunit)
        self.assertEqual(Generator(1, Running()), powerunit)
