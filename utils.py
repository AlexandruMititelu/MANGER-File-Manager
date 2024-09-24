from typing import Set  # Allows type hinting for sets

def is_valid_filename(file_path: str) -> bool:
    return file_path.strip().isnumeric() or any(char.isdigit() for char in file_path)  # Check if the filename is valid

def extract_numbers(file_name: str) -> str:
    return ''.join(filter(str.isdigit, file_name))  # Extract and return only the digits from the filename

def read_input_text(input_text: str) -> Set[str]:
    return set(map(extract_numbers, filter(is_valid_filename, input_text.split('\n'))))  # Process input text and return a set of valid filenames