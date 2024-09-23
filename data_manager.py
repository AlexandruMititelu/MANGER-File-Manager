import json
from pathlib import Path

DATA_FILE = 'user_data.json'

def save_data(source_path: str, target_path: str, input_text: str):
    data = {
        'source_path': source_path,
        'target_path': target_path,
        'input_text': input_text
    }
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def load_data():
    if Path(DATA_FILE).exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {'source_path': '', 'target_path': '', 'input_text': ''}