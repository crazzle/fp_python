import unittest
from operator import add

"""
Aufgabe 4:
Den Term parsen und aufsummieren

Konkret:
Wir haben nun Higher-Order-Functions kennengelernt und ein eigenes "reduce" 
geschrieben. "reduce" soll verwendet werden um den String aufzusummieren.

Signatur von reduce:
def reduce(f, sequence, initial=None)

Beispiel:
"78+67+65" = 210
"""


class Testsuite(unittest.TestCase):

    zahlen = "78+101+118+101+114+32+67+111+100+101+32+65+108+111+110+101"
    problematisch = "++78+101+118+101+114+32+67++111+100+101+32+65+108+111++++110+101"
    ergebnis = 1450

    def test(self):
        self.assertEqual(self.ergebnis, reduce(add, map(int, self.zahlen.split("+"))))
        self.assertEqual(self.ergebnis, reduce(add, map(int, filter(bool, self.problematisch.split("+")))))
