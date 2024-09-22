import os
import shutil
import re

from pathlib import Path

# Asking user to input the folder containing all the photos
# file_path_all_photos = input("Enter the path where all the photos are located: ")
file_path_all_photos = "D:\Photos 12\SRVU Board 2024 Sept"

# Asking user to input the destination folder
# destination_path = input("Enter the path where the selected photos should be stored: ")
destination_path = "D:\Photos 12\SRVU selected"

# Asking user to input the parts of the filenames or numbers
file_names_to_select = input("Enter the parts of the file names or numbers to select (separated by commas, newlines, or including 'JPG'/'jpg'): ")

# Normalize the input by replacing 'JPG'/'jpg' with an empty string and splitting by commas or newlines
file_names_to_select = re.split(r'[,\n]+', file_names_to_select)

# Extract numeric parts and remove '.jpg' or '.JPG'
file_numbers_to_select = [
    name.strip().replace('.jpg', '').replace('.JPG', '') 
    for name in file_names_to_select
]

# file_numbers_to_select = [
#     name.strip() for name in file_names_to_select
# ]

# Output the numbers from the input, separated by commas
print(f"Selected patterns: '{', '.join(file_numbers_to_select)}'")

# Ensure the destination directory exists, create if it doesn't
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

# Copy the files that match the given patterns
for file_name in os.listdir(file_path_all_photos):
    for pattern in file_numbers_to_select:
        if pattern in file_name:
            source = os.path.join(file_path_all_photos, file_name)
            destination = os.path.join(destination_path, file_name)

            # Copy the file, keeping the extension
            shutil.copy(source, destination)
            print(f"Copied {file_name} to {destination_path}")
            break  # Exit the loop once a match is found

print("Files have been copied successfully!")
