import gems.cactus as cactus
import json

def json_print(value):
  print(json.dumps(value, indent=2))

print()
print("TEST: _deep_munge")
print(cactus._deep_munge(5, 6))
print(cactus._deep_munge(5, "cactus.notFound"))
print(cactus._deep_munge([1, 2], [2, 3]))
print(cactus._deep_munge([], [2, 3]))
print(cactus._deep_munge({"a": 1, "b": 2, "x": {"n": 22}}, {"b":3, "c":4}))

print()
print("TEST: _gets")
print(cactus._gets(5, []))
print(cactus._gets({"a": 1}, ["a"]))
print(cactus._gets({"a": 1}, ["x"]))
try:
  print(cactus._gets(5, ["x"]))
except AttributeError:
  print("AttributeError")

"""
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
d2.update({"j": {"w": 33}})
print(json.dumps(d3, indent=2))
print(cactus.gets(d3,[]))
print(cactus.gets(d3,["j"]))
print(cactus.gets(d3,["j", "w"]))
print(cactus.gets(d3,["q", "w"]))
print(cactus.gets(d3,["j", "r"]))
try:
  print(cactus.gets(d3,["j", "w", "x"]))
except AttributeError:
  print("oops")
"""
