import gems.cactus as cactus
print(cactus.resolve(None, "x"))
d1 = {"a": 1}
print(cactus.resolve(d1, "x"))
print(cactus.resolve(d1, "a"))
d2 = {"cactus.next": d1, "b": 2}
print(cactus.resolve(d2, "a"))
print(cactus.flatten(None))
print(cactus.flatten(d1))
print(cactus.flatten(d2))
d3 = {"cactus.next": d2, "a": 23}
print(cactus.flatten(d3))
