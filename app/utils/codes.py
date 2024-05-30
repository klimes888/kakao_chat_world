# codes.py
import json


def load_codes(filepath="./codes.json"):
    with open(filepath, "r") as file:
        codes = json.load(file)
    return codes


codes = load_codes()
