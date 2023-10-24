def gen_gem_types(level):
  gem_types = {}
  level.update({"gem.types": gem_types})

def gen_root():
  root = {"cactus.name": "root"}
  gen_gem_types(root)
  return root
