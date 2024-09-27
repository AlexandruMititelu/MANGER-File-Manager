import json  # Standard library for JSON serialization and deserialization
import os  # Import os to handle file operations
from pathlib import Path  # For handling filesystem paths

DATA_FILE = os.path.join(os.path.dirname(__file__), 'user_data.json')

def hide_file(file_path: str):
    if os.name == 'nt':  # For Windows
        os.system(f'attrib +h "{file_path}"')  # Hide the file on Windows
    else:  # For Unix/Linux/Mac
        os.system(f'chflags hidden "{file_path}"')  # Hide the file on Unix-like systems

def save_data(source_path: str, target_path: str, input_text: str):
    data = {
        'source_path': source_path,  # Store the source path
        'target_path': target_path,  # Store the target path
        'input_text': input_text  # Store the input text
    }
    with open(DATA_FILE, 'w') as f:  # Open the data file for writing
        json.dump(data, f)  # Write the data to the file
    hide_file(DATA_FILE)  # Hide the file after saving

def load_data():
    if Path(DATA_FILE).exists():  # Check if the data file exists
        with open(DATA_FILE, 'r') as f:  # Open the data file for reading
            return json.load(f)  # Load and return the data
    return {'source_path': '', 'target_path': '', 'input_text': ''}  # Return default values if the file doesn't exist