import gems.build as build
import gems.operations as operations

root = build.root()

def ribbit(cactus):
  print("Ribbit!")
  
operations.ops["ribbit"] = ribbit

operations.ops["ribbit"](root)