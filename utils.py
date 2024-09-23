from typing import Set

def is_valid_filename(file_path: str) -> bool:
    return file_path.strip().isnumeric() or any(char.isdigit() for char in file_path)

def extract_numbers(file_name: str) -> str:
    return ''.join(filter(str.isdigit, file_name))

def read_input_text(input_text: str) -> Set[str]:
    return set(map(extract_numbers, filter(is_valid_filename, input_text.split('\n'))))