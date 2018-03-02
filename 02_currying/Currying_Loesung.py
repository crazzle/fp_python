def curried(func):
    def curry(*args):
        if len(args) == func.__code__.co_argcount:
            ans = func(*args)
            return ans
        else:
            return lambda x: curry(*(args+(x,)))

    return curry

@curried
def test(a, b, c, d):
    print a
    print b
    print c
    print d

testABC = test("a", "b", "c")
print "Now!"
testABC("d")

