import unittest
from operator import add

"""
Aufgabe 3:
Eine Liste von Zahlen aufsummieren

Beispiel:
[78, 67, 65] = 210

"""


class Testsuite(unittest.TestCase):

    zahlen = [78, 101, 118, 101, 114, 32, 67, 111, 100, 101, 32, 65, 108, 111, 110, 101]
    ergebnis = 1450

    def test(self):
        self.assertEqual(self.ergebnis, summiere_iterativ(self.zahlen))
        self.assertEqual(self.ergebnis, foldRight(add, 0, self.zahlen))
        self.assertEqual(self.ergebnis, foldLeft(add, 0, self.zahlen))
        self.assertEqual(self.ergebnis, sum(self.zahlen))


def summiere_iterativ(zahlen):
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
