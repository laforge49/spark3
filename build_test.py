import gems.build as build
import json

root = build.root()
print(json.dumps(root, indent=2))
