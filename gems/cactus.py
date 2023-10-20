# A cactus is a tree of dict linked by the key "cactus.next".

# Find the first matching key in a stack of dict.
def resolve(leaf, key):
  if leaf == None:
    return None
  value = leaf.get(key)
  if value == None:
    return resolve(leaf.get("cactus.next"), key)
  return value
  
# Create a dict with all the effective values of a stack of dict.
def flatten (leaf):
  if (leaf == None):
    return {}
  next = leaf.get("cactus.next")
  base = flatten(next)
  base.update(leaf)
  base.pop("cactus.next", None)
  return base
  