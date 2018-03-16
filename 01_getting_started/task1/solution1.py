import unittest


"""
Task 1:
Convert the string into a string of ASCII codes 

Detail:
Convert the string into a string of ASCII codes concatenated
by '+'

Example:
NCA = "78+67+65"

Characters can be converted to ASCII by ord()
"""


class Testsuite(unittest.TestCase):
    the_string = "Never Code Alone"
    result = "78+101+118+101+114+32+67+111+100+101+32+65+108+111+110+101"

    def test(self):
        self.assertEqual(self.result, convert(self.the_string))
        self.assertEqual(self.result, convert_recursive(self.the_string))
        self.assertEqual(self.result, convert_comprehension(self.the_string))
        self.assertEqual(self.result, convert_map(self.the_string))


def convert(zeile):
    zahlen = ""
    for i in range(0, len(zeile)):
        zahl = str(ord(zeile[i]))
        zahlen += zahl
        if i < len(zeile)-1:
            zahlen += "+"
    return zahlen


def convert_recursive(zeile):
    if len(zeile) > 1:
        return str(ord(zeile[0])) + "+" + convert_recursive(zeile[1:])
    else:
        return str(ord(zeile[0]))


def convert_comprehension(zeile):
    return "+".join([str(ord(buchstabe)) for buchstabe in zeile])


def convert_map(zeile):
    return "+".join(map(lambda b: str(ord(b)), zeile))





