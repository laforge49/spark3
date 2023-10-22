'''
A cactus is a tree of dict linked by the key "cactus.next".
This can be used as a universal API that supports
1. Transparent parameter passing to low-level functions.
2. The use of default values and overrides.
3. Run-time scoping of parameters and the ability to update them.
'''

import copy
import collections.abc

# Create a new jason structure from the prior structure by applying 
# the changes in the revision structure. The changes are largely
# replacements, though revisions to a list serve to extend the
# prior list.
#
# If the revision is a dict, any items present in the prior dict
# not present in the revision are added to the revision.
#
# If the revision and prior are both lists, the prior is inserted at the 
# start of revision.
def _deepmunge(prior, revision):
  if revision == "cactus.notFound":
    return copy.deepcopy(prior)
  if isinstance(revision, collections.abc.Mapping):
    if isinstance(prior, collections.abc.Mapping):
      for key, value in prior.items:
        revision[key] = _deepmunge(value, revision.get(key, "cactus.notFound"))
        return revision
  elif isinstance(revision, list):
    if isinstance(prior, list):
      for n in range(len(prior),-1,-1):
        revision.insert(0,prior[n])
      return revision
  else:
    return revision
  
# Get the first matching key in a stack of dict.
def resolve(leaf, key):
  if leaf == None:
    return None
  value = leaf.get(key, "cactus.notFound")
  if value == "cactus.notFound":
    return resolve(leaf.get("cactus.next"), key)
  return value
  
def gets(leaf, keys):
  if len(keys) == 0:
    return None
  j = resolve(leaf, keys[0])
  for key in keys[1:]:
    if j == None:
      return None
    j = j.get(key, None)
  return j
  
def _flatten(leaf):
  if (leaf == None):
    return {}
  next = leaf.get("cactus.next")
  base = flatten(next)
  base.update(leaf)
  return base
  
# Create a dict with all the effective values of a stack of dict.
def flatten(leaf):
  base = _flatten(leaf)
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

# Rewind to a lower-level dict
def rewind(leaf, level):
  if leaf == None:
    return None
  if level == 0:
    return leaf
  next = leaf.get("cactus.next")
  return rewind(next, level - 1)
  