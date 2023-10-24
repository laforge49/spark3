import gems.build as build
import json

root = build.gen_root()
print(json.dumps(root, indent=2))
