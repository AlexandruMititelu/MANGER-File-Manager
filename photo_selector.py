import os  # Provides functions for interacting with the operating system
import shutil  # Offers high-level file operations like copying
import logging  # Used for logging messages for debugging and tracking
from pathlib import Path  # Provides an object-oriented interface for filesystem paths
from typing import Set  # Allows type hinting for sets

def copy_selected_files(source_dir: Path, dest_dir: Path, file_names_to_select: Set[str]) -> int:
    counter = 0  # Initialize a counter for copied files
    for file_name in os.listdir(source_dir):  # Iterate through files in the source directory
        if any(pattern in file_name for pattern in file_names_to_select):  # Check if file matches any selected patterns
            source = source_dir / file_name  # Create the full path for the source file
            destination = dest_dir / file_name  # Create the full path for the destination file
            try:
                shutil.copy2(source, destination)  # Copy the file to the destination
                logging.info(f"Copied {file_name} to {dest_dir}")  # Log the successful copy
                counter += 1  # Increment the counter
            except (shutil.SameFileError, PermissionError, OSError) as e:  # Handle specific exceptions
                logging.error(f"Error copying {file_name}: {e}")  # Log the error
    return counter  # Return the number of files copied