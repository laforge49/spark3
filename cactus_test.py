import gems.cactus as cactus
import json
print(cactus.resolve(None, "x"))
d1 = {"a": 1, "cactus.name": "root"}
print(cactus.resolve(d1, "x"))
print(cactus.resolve(d1, "a"))
d2 = {"cactus.next": d1, "b": 2}
print(cactus.resolve(d2, "a"))
print(cactus.flatten(None))
print(cactus.flatten(d1))
print(cactus.flatten(d2))
d3 = {"cactus.next": d2, "a": 23, "b": None}
print(cactus.resolve(d3, "b"))
print(cactus.flatten(d3))
print(cactus.named(d3, "xyz"))
print(cactus.named(d3, "root"))
print(cactus.rewind(d3, 1))
print(json.dumps(d3, indent=2))
