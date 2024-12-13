import json
import os

def restore_all_books(all_books):
    # Get the directory of the current script
    file_path = os.path.join(os.path.dirname(__file__), "all_books.json")
    try:
        with open(file_path, "r") as fp:
            all_books = json.load(fp)
            print("Books loaded successfully.")
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found. Initializing an empty book list.")
        all_books = []
    except json.JSONDecodeError:
        print(f"Error: Could not parse the JSON file. Check the content of '{file_path}'.")
        all_books = []
    return all_books
