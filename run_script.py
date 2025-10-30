import json

data = {"message": "Hello from Python!", "status": "success"}

with open("output.json", "w") as f:
    json.dump(data, f)

print("Done writing output.json")
