import unittest


"""
Aufgabe 4:
End-2-End - String aufsummieren mit fold!

Konkret:
Wir haben nun Higher-Order-Functions kennengelernt und ein eigenes "reduce" (fold)
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
        self.assertEqual(self.ergebnis, self.zahlen)
        self.assertEqual(self.ergebnis, self.problematisch)

