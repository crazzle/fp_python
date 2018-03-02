import unittest

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
        self.assertEqual(self.ergebnis, summiere(self.zahlen))


def summiere(zahlen):
    pass


