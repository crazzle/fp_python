from collections import namedtuple
from operator import add, sub

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

'''
Definieren der State-Actions
'''
unit = lambda generator: ((generator.output, generator.state), generator)

'''
State Transition
'''
def action(target, generator):
    output, state = generator
    if target == output:
        return (output, state), Generator(target, Running())
    elif target < output:
        return (output, state), Generator(sub(output, 1), Dispatching())
    elif target > output:
        return (output, state), Generator(add(output, 1), Dispatching())


'''
Testen
'''
powerunit = Generator(0, Running())
print unit(powerunit)

_, powerunit = action(5, powerunit)
_, powerunit = action(5, powerunit)
_, powerunit = action(5, powerunit)
_, powerunit = action(5, powerunit)
_, powerunit = action(5, powerunit)
_, powerunit = action(5, powerunit)
print powerunit

_, powerunit = action(3, powerunit)
_, powerunit = action(3, powerunit)
_, powerunit = action(3, powerunit)
print powerunit

_, powerunit = action(0, powerunit)
_, powerunit = action(0, powerunit)
_, powerunit = action(0, powerunit)
_, powerunit = action(1, powerunit)
_, powerunit = action(1, powerunit)
print powerunit

'''
Testen mit fold
'''
replay = "4+4+4+3+3+3+3+5+5+5+5+5+1+1+1+1+1+1+0+0"
unit = Generator(0, Running())
unit = foldLeft(lambda acc, el: action(acc, el)[1], unit, map(int, replay.split('+')))
print unit