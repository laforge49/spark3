import gems.cactus
print(gems.cactus.resolve(None, "x"))
d1 = {"a": 1}
print(gems.cactus.resolve(d1, "x"))
print(gems.cactus.resolve(d1, "a"))
d2 = {"cactus.next": d1}
print(gems.cactus.resolve(d2, "a"))
