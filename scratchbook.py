def dct(*items):
    def pair((key, value)):
        return lambda k: value if k == key else None

    def merge(l, r):
        return lambda k: l(k) or r(k)

    return reduce(merge, map(pair, items), pair((None,None)))


d = dct(("john","dow"), ("matt","wills"), ("john","cow"), ("mark","douglas"), ("beever","scythe"))

print d("john")
#print d("john")
#print d("matt")
#print d("beever")

x = lambda x,y,z: x or y or z

print x(None, "b", "c")
print x("a", None, "c")
print x(None, None, "c")


def foldRight(f, z, items):
    if not items:
        return z
    else:
        head, tail = items[0], items[1:]
        return f(head, foldRight(f, z, tail))


print foldRight(lambda a,b: a+b, 0, [1, 2, 4])

code = "67+79+68+69+33"
start = "78+101+118+101+114+32+67+111+100+101+32+65+108+111+110+101"
str = "Never Code Alone"

print reduce(lambda l,r: l+ "+" + r, map(lambda s: "%s" % ord(s), "NCA"))

print sum(map(lambda s: int(s), start.split("+")))
