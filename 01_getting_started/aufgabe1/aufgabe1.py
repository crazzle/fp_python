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


def convert(row):
    pass





