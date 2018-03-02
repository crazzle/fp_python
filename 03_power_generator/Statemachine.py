from collections import namedtuple
from operator import add, sub

"""
Function Currying:
Wir bauen einen kleinen Generator.
Der Generator liefert per Default 0kw.
Gibt man ihm ein Target nähert er sich diesem Target nach und nach an
bis er es erreicht.
"""

'''
Helper Funktionen
'''
def foldRight(f, acc, items):
    if not items:
        return acc
    else:
        head, tail = items[0], items[1:]
        return f(head, foldRight(f, acc, tail))


def foldLeft(f, acc, items):
    if not items:
        return acc
    else:
        head, tail = items[0], items[1:]
        return foldLeft(f, f(head, acc), tail)

'''
Definieren unserer States
'''
Generator = namedtuple("Generator", ["output", "state"])
Running = namedtuple("Running", [])
Dispatching = namedtuple("Dispatching", [])
