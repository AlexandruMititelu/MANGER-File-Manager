import os
import shutil
import logging
from pathlib import Path
from typing import Set

file_path_all_photos = "D:\Photos 12\SRVU Board 2024 Sept"
destination_path = "D:\Photos 12\SRVU selected"

def is_valid_filename(file_path: str) -> bool:
    # A valid filename is either numeric or contains at least one digit
    return file_path.strip().isnumeric() or any(char.isdigit() for char in file_path)

def extract_numbers(file_name: str) -> str:
    return ''.join(filter(str.isdigit, file_name))

def read_input_file(input_file: str = 'input') -> Set[str]:
    try:
        with open(input_file, 'r') as file:
            return set(map(extract_numbers, filter(is_valid_filename, file.readlines())))
    except FileNotFoundError:
        logging.error(f"Error: The '{input_file}' file does not exist.")
        raise
    except Exception as e:
        logging.error(f"An error occurred while reading the '{input_file}' file: {e}")
        raise

def copy_selected_files(source_dir: Path, dest_dir: Path, file_names_to_select: Set[str]) -> int:
    counter = 0
    for file_name in os.listdir(source_dir):
        # Check if any pattern in the set of filenames to select is in the current filename
        if any(pattern in file_name for pattern in file_names_to_select):
            source = source_dir / file_name  # Construct the source file path
            destination = dest_dir / file_name  # Construct the destination file path
            try:
                shutil.copy2(source, destination)
                logging.info(f"Copied {file_name} to {dest_dir}")
                counter += 1
            except (shutil.SameFileError, PermissionError, OSError) as e:
                logging.error(f"Error copying {file_name}: {e}")
    return counter

def main():
    # Configure the logging module to display info level messages with a specific format
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Create Path objects for the source and destination directories
        source_dir = Path(file_path_all_photos)
        dest_dir = Path(destination_path)

        if not source_dir.exists():
            raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.")
        
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        
        file_names_to_select = read_input_file()
        files_copied = copy_selected_files(source_dir, dest_dir, file_names_to_select)
        
        logging.info(f"Files have been copied successfully! {files_copied} photos have been selected")
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()