def printer():
  print("this is cactus")
  
def resolve(leaf, key):
  if leaf == None:
    return None
  value = leaf.get(key)
  if value == None:
    return resolve(leaf.get("cactus.next"), key)
  return value