import gems.cactus as cactus
import json

def json_print(value):
  print(json.dumps(value, indent=2))

print()
print("1. TEST _deep_munge")
print("1.1", cactus._deep_munge(5, 6))
print("1.2", cactus._deep_munge(5, "cactus.notFound"))
print("1.3", cactus._deep_munge([1, 2], [2, 3]))
print("1.4", cactus._deep_munge([], [2, 3]))
print("1.5", cactus._deep_munge({"a": 1, "b": 2, "x": {"n": 22}}, {"b":3, "c":4}))

print()
print("2. TEST _gets")
print("2.1", cactus._gets(5, []))
print("2.2", cactus._gets({"a": 1}, ["a"]))
print("2.3", cactus._gets({"a": 1}, ["x"]))
try:
  print("2.4", cactus._gets(5, ["x"]))
except AttributeError:
  print("2.4 Attribute Error")

print()
print("3. TEST DATA")
d1 = {"a": 1, "cactus.name": "root"}
d2 = {"cactus.next": d1, "b": 2, "c": [2], "d": {"q": 8, "r": 64}}
d3 = {"cactus.next": d2, "a": 23, "b": None, "c": [3], "d": {"q": 9, "s": 99}}
print(json.dumps(d3, indent=2))

print()
print("4. TEST flatten")
print("4.1", cactus.flatten(None))
print("4.2", cactus.flatten(d1))
print("4.3", cactus.flatten(d2))
print("4.4", cactus.flatten(d3))

print()
print("5. TEST resolves")
print("5.1", cactus.resolves(None, ["x"]))
print("5.2", cactus.resolves(d1, ["x"]))
print("5.3", cactus.resolves(d1, ["a"]))
print("5.4", cactus.resolves(d2, ["a"]))
print("5.5", cactus.resolves(d3, ["a"]))
print("5.6", cactus.resolves(d3, ["b"]))
print("5.6", cactus.resolves(d3, ["c"]))
print("5.7", cactus.resolves(d3, ["d"]))
print("5.8", cactus.resolves(d3, ["d", "q"]))

print()
print("6. TEST named")
print("6.1", cactus.named(d3, "xyz"))
print("6.2", cactus.named(d3, "root"))

print()
print("7. TEST rewind")
print("7.1", cactus.rewind(d3, 1))

print()
print("8. TEST puts")
d4 = {}
cactus.puts(d4, ["a"], 1)
print("8.1", d4)
cactus.puts(d4, ["b"], {"c": 2})
print("8.2", d4)
cactus.puts(d4, ["b", "d"], 39)
print("8.3", d4)
cactus.puts(d3, ["a"], 2)
print("8.4", d3)
cactus.puts(d3, ["g"], 21)
print("8.5", d3)
cactus.puts(d3, ["c"], [40])
print("8.6", d3)
cactus.puts(d3, ["d", "n"], 5)
print("8.7", d3)
