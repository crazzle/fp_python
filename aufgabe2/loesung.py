import unittest


"""
Aufgabe 2:
Zahlen-Strings in Integer konvertieren

Konkret:
Die Zahlen im String sollen in Integer konvertiert werden

Beispiel:
"78+67+65" = [78, 67, 65]

"""


class Testsuite(unittest.TestCase):
    zahlen = "78+101+118+101+114+32+67+111+100+101+32+65+108+111+110+101"
    ergebnis = [78, 101, 118, 101, 114, 32, 67, 111, 100, 101, 32, 65, 108, 111, 110, 101]

    def test(self):
        assert konvertiere(self.zahlen) == self.ergebnis


def konvertiere(zahlen):
    return map(int, zahlen.split("+"))