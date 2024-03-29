import gems.cactus as cactus
import json

def json_print(value):
  print(json.dumps(value, indent=2))

print()
print("1. TEST _deep_munge")

print("1.1", cactus._deep_munge(5, 6))
# Output:
# 1.1 6

print("1.2", cactus._deep_munge(5, "cactus.notFound"))
# Output:
# 1.2 5

print("1.3", cactus._deep_munge([1, 2], [2, 3]))
# Output:
# 1.3 [1, 2, 2, 3]

print("1.4", cactus._deep_munge([], [2, 3]))
# Output:
# 1.4 [2, 3]

print("1.5", cactus._deep_munge({"a": 1, "b": 2, "x": {"n": 22}}, {"b":3, "c":4}))
# Output:
# 1.5 {'b': 3, 'c': 4, 'a': 1, 'x': {'n': 22}}

print()
print("2. TEST _gets")

print("2.1", cactus._gets(5, []))
# Output:
# 2.1 5

print("2.2", cactus._gets({"a": 1}, ["a"]))
# Output:
# 2.2 1

print("2.3", cactus._gets({"a": 1}, ["x"]))
# Output:
# 2.3 cactus.notFound

try:
  print("2.4", cactus._gets(5, ["x"]))
except AttributeError:
  print("2.4 Attribute Error")
# Output:
# 2.4 Attribute Error

print()
print("3. TEST DATA")
d1 = {"a": 1, "cactus.name": "root"}
d2 = {"cactus.next": d1, "b": 2, "c": [2], "d": {"q": 8, "r": 64}}
d3 = {"cactus.next": d2, "a": 23, "b": None, "c": [3], "d": {"q": 9, "s": 99}}

json_print(d3)
"""
 Output:
{
  "cactus.next": {
    "cactus.next": {
      "a": 1,
      "cactus.name": "root"
    },
    "b": 2,
    "c": [
      2
    ],
    "d": {
      "q": 8,
      "r": 64
    }
  },
  "a": 23,
  "b": null,
  "c": [
    3
  ],
  "d": {
    "q": 9,
    "s": 99
  }
}
"""

print()
print("4. TEST flatten")

print("4.1", cactus.flatten(None))
# Output:
# 4.1 {}

print("4.2", cactus.flatten(d1))
# Output:
# 4.2 {'a': 1}

print("4.3", cactus.flatten(d2))
# Output:
# 4.3 {'b': 2, 'c': [2], 'd': {'q': 8, 'r': 64}, 'a': 1}

print("4.4", cactus.flatten(d3))
# Output:
# 4.4 {'a': 23, 'b': None, 'c': [2, 3], 'd': {'q': 9, 's': 99, 'r': 64}}

print()
print("5. TEST resolves")

print("5.1", cactus.resolves(None, ["x"]))
# Output:
# 5.1 cactus.notFound

print("5.2", cactus.resolves(d1, ["x"]))
# Output:
# 5.2 cactus.notFound

print("5.3", cactus.resolves(d1, ["a"]))
# Output:
# 5.3 1

print("5.4", cactus.resolves(d2, ["a"]))
# Output:
# 5.4 1

print("5.5", cactus.resolves(d3, ["a"]))
# Output:
# 5.5 23

print("5.6", cactus.resolves(d3, ["b"]))
# Output:
# 5.6 None

print("5.7", cactus.resolves(d3, ["c"]))
# Output:
# 5.7 [2, 3]

print("5.8", cactus.resolves(d3, ["d"]))
# Output:
# 5.8 {'q': 9, 's': 99, 'r': 64}
print("5.9", cactus.resolves(d3, ["d", "q"]))
# Output:
# 5.9 9

print()
print("6. TEST named")

print("6.1", cactus.named(d3, "xyz"))
# Output:
# 6.1 None

print("6.2", cactus.named(d3, "root"))
# Output:
# 6.2 {'a': 1, 'cactus.name': 'root'}

print()
print("7. TEST rewind")

print("7.1", cactus.rewind(d3, 1))
# Output:
# 7.1 {'cactus.next': {'a': 1, 'cactus.name': 'root'}, 'b': 2, 'c': [2], 'd': {'q': 8, 'r': 64}}

print()
print("8. TEST puts")
d4 = {}

cactus.puts(d4, ["a"], 1)
print("8.1", d4)
# Output:
# 8.1 {'a': 1}

cactus.puts(d4, ["b"], {"c": 2})
print("8.2", d4)
# Output:
# 8.2 {'a': 1, 'b': {'c': 2}}

cactus.puts(d4, ["b", "d"], 39)
print("8.3", d4)
# Output:
# 8.3 {'a': 1, 'b': {'c': 2, 'd': 39}}

cactus.puts(d3, ["a"], 2)
print("8.4", cactus.flatten(d3))
# Output:
# 8.4 {'a': 2, 'b': None, 'c': [2, 3], 'd': {'q': 9, 's': 99, 'r': 64}}

cactus.puts(d3, ["g"], 21)
print("8.5", cactus.flatten(d3))
# Output:
# 8.5 {'a': 2, 'b': None, 'c': [2, 3], 'd': {'q': 9, 's': 99, 'r': 64}, 'g': 21}

cactus.puts(d3, ["c"], [40])
print("8.6", cactus.flatten(d3))
# Output:
# 8.6 {'a': 2, 'b': None, 'c': [2, 3, 40], 'd': {'q': 9, 's': 99, 'r': 64}, 'g': 21}

cactus.puts(d3, ["d", "n"], 5)
print("8.7", cactus.flatten(d3))
# Output:
# 8.7 {'a': 2, 'b': None, 'c': [2, 3, 40], 'd': {'q': 9, 's': 99, 'n': 5, 'r': 64}, 'g': 21}
