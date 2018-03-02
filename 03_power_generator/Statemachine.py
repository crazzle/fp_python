from collections import namedtuple
import unittest

"""
Function Currying:
Wir bauen einen kleinen Generator.
Der Generator liefert per Default 0kw.
Gibt man ihm ein Target naehert er sich diesem Target nach und nach an
bis er es erreicht.
"""


'''
Helper Funktionen
'''
def foldLeft(f, acc, items):
    if not items:
        return acc
    else:
        head, tail = items[0], items[1:]
        return foldLeft(f, f(head, acc), tail)

'''
Definieren unserer States
'''
Generator = namedtuple("Generator", ["output", "state"])
Running = namedtuple("Running", [])
Dispatching = namedtuple("Dispatching", [])

'''
Definieren der State-Transition

Signatur:
target, generator -> (Int, State), Generator
'''
def action(target, generator):
    pass

class Testsuite(unittest.TestCase):
    replay = "4+4+4+3+3+3+3+5+5+5+5+5+1+1+1+1+1+1"
    ergebnis = Generator(output=1, state=Running())

    def test_statemachine(self):
        self.fail("Not implemented yet")

    def test_fold(self):
        self.assertEqual(self.ergebnis, None)



