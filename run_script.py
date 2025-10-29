# # run_script.py
# import json

# def main():
#     print(json.dumps({"message": "Hello from GitHub!"}))

# if __name__ == "__main__":
#     main()
import json

data = {"message": "Hello from Python!", "status": "success"}

with open("output.json", "w") as f:
    json.dump(data, f)

print("Done writing output.json")
