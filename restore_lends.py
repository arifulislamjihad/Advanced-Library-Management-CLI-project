import json
import os

def restore_lends():
    file_path = os.path.join(os.path.dirname(__file__), "lend_books.json")
    try:
        with open(file_path, "r") as fp:
            return json.load(fp)
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found. Initializing an empty lend list.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not parse the JSON file. '{file_path}' is empty or invalid. Initializing an empty lend list.")
        return []
