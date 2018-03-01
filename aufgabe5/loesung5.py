import unittest


"""
Aufgabe 5:
Funktionen koennen auch Funktionen zurueckgeben.
Mit "reduce" kann man noch viel mehr machen wenn das Ergebnis 
eine Funktion ist.
Wie sieht es zum Beispiel mit einem "Functional"-Dictionary aus? 
"""

paare = [("n", "never"), ("c", "code"), ("a", "alone")]

class Testsuite(unittest.TestCase):
    ergebnis = dict(paare)

    def test(self):
        self.assertEqual(self.ergebnis["n"], get("n"))
        self.assertEqual(self.ergebnis["c"], get("c"))
        self.assertEqual(self.ergebnis["a"], get("a"))


def get(key):
    return store(paare)(key)


def store(items):
    def pair((key, value)):
        return lambda k: value if k == key else None

    def merge(l, r):
        return lambda k: l(k) or r(k)

    return reduce(merge, map(pair, items), pair((None,None)))