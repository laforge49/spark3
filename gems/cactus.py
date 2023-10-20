# A cactus is a tree of dict linked by the key "cactus.next".

# Find the first matching key in a stack of dict.
def resolve(leaf, key):
  if leaf == None:
    return None
  value = leaf.get(key, "cactus.notFound")
  if value == "cactus.notFound":
    return resolve(leaf.get("cactus.next"), key)
  return value
  
def flatten_(leaf):
  if (leaf == None):
    return {}
  next = leaf.get("cactus.next")
  base = flatten(next)
  base.update(leaf)
  return base
  
# Create a dict with all the effective values of a stack of dict.
def flatten(leaf):
  base = flatten_(leaf)
  base.pop("cactus.next", None)
  base.pop("cactus.name", None)
  return base

# Returns the named dict in the stack of dict.
def named(leaf, name):
  if leaf == None:
    return None
  if name == leaf.get("cactus.name"):
    return leaf
  return named(leaf.get("cactus.next"), name)
  