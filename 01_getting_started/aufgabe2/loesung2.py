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
        self.assertListEqual(self.ergebnis, konvertiere(self.zahlen.split("+")))
        self.assertListEqual(self.ergebnis, map(int, self.zahlen.split("+")))


def konvertiere(zahlen):
    def custom_map(f, list):
        if len(list) > 1:
            c = [f(list[0])]
            c.extend(custom_map(f, list[1:]))
            return c
        return [f(list[0])]
    return custom_map(int, zahlen)
