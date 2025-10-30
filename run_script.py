import json
import sys


def main():
    try:
        # Try to read input file (if it exists)
        input_data = {}
        if len(sys.argv) > 1:
            input_path = sys.argv[1]
            try:
                with open(input_path, "r") as f:
                    input_data = json.load(f)
            except Exception:
                input_data = {"warning": f"Could not read input file: {input_path}"}

        # ✅ Do your processing logic here
        data = {
            "message": "Hello from Python!",
            "status": "success",
            "received_input": input_data,
        }

        # ✅ Write result to output.json
        with open("output.json", "w") as f:
            json.dump(data, f, indent=2)

        print("✅ Done writing output.json")

    except Exception as e:
        # In case anything fails, create an error output
        with open("output.json", "w") as f:
            json.dump({"error": str(e)}, f)
        print(f"❌ Error occurred: {e}")


if __name__ == "__main__":
    main()
