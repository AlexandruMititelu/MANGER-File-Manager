import json  
import os  
from pathlib import Path  

DATA_FILE = os.path.join(os.path.dirname(__file__), 'user_data.json')

def hide_file(file_path: str):
    if os.name == 'nt':  # For Windows
        os.system(f'attrib +h "{file_path}"')  # also hides the file
    else:  # For Unix/Linux/Mac
        os.system(f'chflags hidden "{file_path}"')  

def save_data(source_path: str, target_path: str, input_text: str):
    data = {
        'source_path': source_path,  
        'target_path': target_path,  
        'input_text': input_text  
    }
    with open(DATA_FILE, 'w') as f:  
        json.dump(data, f)  # Write the data to the file
    hide_file(DATA_FILE)  

def load_data():
    if Path(DATA_FILE).exists():  # Check if the data file exists
        with open(DATA_FILE, 'r') as f:  # Open the data file for reading
            return json.load(f)  # Load and return the data
    return {'source_path': '', 'target_path': '', 'input_text': ''}  # Return default values if the file doesn't exist