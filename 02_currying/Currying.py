import unittest

"""
Function Currying:
Wir bauen einen Decorator "Curry" der Funktionen
partiell anwendet und uns eine neue Funktion wiedergibt.

Hilfe:
Ein Dekorator ist eine Funktion, die eine Funktion uebergeben
bekommt. Die uebergebene Funktion wird gewrapped.

<Function>.__code__.co_argcount gibt die Anzahl der Parameter
eines Funktionsobjekts zurueck
"""


def curried(func):
    def curry(*args):
        pass
    return curry


@curried
def test(a, b, c):
    return a+b+c


class Testsuite(unittest.TestCase):
    ergebnis = 6

    def test(self):
        test1 = test(1)
        test2 = test1(2)
        self.assertEqual(self.ergebnis, test2(3))
