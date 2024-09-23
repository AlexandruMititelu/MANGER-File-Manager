import os
import shutil
import logging
from pathlib import Path
from typing import Set

def copy_selected_files(source_dir: Path, dest_dir: Path, file_names_to_select: Set[str]) -> int:
    counter = 0
    for file_name in os.listdir(source_dir):
        if any(pattern in file_name for pattern in file_names_to_select):
            source = source_dir / file_name
            destination = dest_dir / file_name
            try:
                shutil.copy2(source, destination)
                logging.info(f"Copied {file_name} to {dest_dir}")
                counter += 1
            except (shutil.SameFileError, PermissionError, OSError) as e:
                logging.error(f"Error copying {file_name}: {e}")
    return counter