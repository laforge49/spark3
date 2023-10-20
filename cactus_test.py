import gems.cactus as cactus
print(cactus.resolve(None, "x"))
d1 = {"a": 1}
print(cactus.resolve(d1, "x"))
print(cactus.resolve(d1, "a"))
d2 = {"cactus.next": d1}
print(cactus.resolve(d2, "a"))
