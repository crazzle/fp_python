import unittest


"""
Aufgabe 1:
Einen String in eine Zeichenkette von Zahlen konvertieren

Konkret:
Konvertiere eine Zeichenfolge in ihren ASCII-Code.
Die einzelnen Zahlenwerte werden durch ein '+'
aneinandergereiht.

Beispiel:
NCA = 78+67+65

Character lassen sich mit ord() in ihren ASCII-Code 
umwandeln.
"""


class Testsuite(unittest.TestCase):
    zeichenkette = "Never Code Alone"
    ergebnis = "78+101+118+101+114+32+67+111+100+101+32+65+108+111+110+101"

    def test(self):
        assert zahlenfolge_iterativ(self.zeichenkette) == self.ergebnis
        assert zahlenfolge_funktional(self.zeichenkette) == self.ergebnis


def zahlenfolge_iterativ(zeile):
    zahlen = ""
    for i in range(0, len(zeile)):
        zahl = str(ord(zeile[i]))
        zahlen += zahl
        if i < len(zeile)-1:
            zahlen += "+"
    return zahlen


def zahlenfolge_funktional(zeile):
    pass








