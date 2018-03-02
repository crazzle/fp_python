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
        self.assertEqual(self.ergebnis, zahlenfolge_iterativ(self.zeichenkette))
        self.assertEqual(self.ergebnis, zahlenfolge_rekursiv(self.zeichenkette))
        self.assertEqual(self.ergebnis, zahlenfolge_comprehension(self.zeichenkette))
        self.assertEqual(self.ergebnis, zahlenfolge_map(self.zeichenkette))
        self.assertEqual(self.ergebnis, zahlenfolge_reduce(self.zeichenkette))


def zahlenfolge_iterativ(zeile):
    zahlen = ""
    for i in range(0, len(zeile)):
        zahl = str(ord(zeile[i]))
        zahlen += zahl
        if i < len(zeile)-1:
            zahlen += "+"
    return zahlen


def zahlenfolge_rekursiv(zeile):
    if len(zeile) > 1:
        return str(ord(zeile[0])) + "+" + zahlenfolge_rekursiv(zeile[1:])
    else:
        return str(ord(zeile[0]))


def zahlenfolge_comprehension(zeile):
    return "+".join([str(ord(buchstabe)) for buchstabe in zeile])


def zahlenfolge_map(zeile):
    return "+".join(map(lambda b: str(ord(b)), zeile))





