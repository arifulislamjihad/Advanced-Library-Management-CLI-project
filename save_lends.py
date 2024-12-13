import json

def save_lends(all_lends):
    with open("lend_books.json", "w") as fp:
        json.dump(all_lends, fp, indent=4)
