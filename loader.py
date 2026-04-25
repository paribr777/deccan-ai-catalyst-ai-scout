import json

def load_candidates():
    with open("candidates_data.json", "r") as f:
        return json.load(f)
