import json
import os


def load_codes(filepath="codes.json"):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, filepath)
    with open(full_path, "r") as file:
        codes = json.load(file)
    return codes


codes = load_codes()
