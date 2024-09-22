import os
import shutil
import re

# from pathlib import Path

def is_valid_filename(file_path):
    # File can is a str that is either an int or a str that must contain at least one digit
    return file_path.isnumeric() or any(char.isdigit() for char in file_path)

# Asking user to input the folder containing all the photos
# file_path_all_photos = input("Enter the path where all the photos are located: ")
file_path_all_photos = "D:\Photos 12\SRVU Board 2024 Sept"

# Asking user to input the destination folder
# destination_path = input("Enter the path where the selected photos should be stored: ")
destination_path = "D:\Photos 12\SRVU selected"

if not os.path.exists(file_path_all_photos):
    print(f"Error: The path '{file_path_all_photos}' does not exist.")
    exit(1)

if not os.path.exists(destination_path):
    print(f"Error: The path '{destination_path}' does not exist.")
    exit(1)

def extract_numbers(file_name) -> str:
    return ''.join(filter(str.isdigit, file_name))
    

# Asking user to input the parts of the filenames or numbers
# file_names_to_select = input("Enter the parts of the file names or numbers to select (separated by commas, newlines, or including 'JPG'/'jpg'): ")
with open('input', 'r') as file:
    file_names_to_select = list(
        map(
            extract_numbers, 
            filter(is_valid_filename, file.readlines())
        )        
    )

# Ensure the destination directory exists, create if it doesn't
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

# Copy the files that match the given patterns
for file_name in os.listdir(file_path_all_photos):
    for pattern in file_names_to_select:
        #print(f"Checking {file_name} for pattern {pattern}")
        if pattern in file_name:
            source = os.path.join(file_path_all_photos, file_name)
            destination = os.path.join(destination_path, file_name)

            # Copy the file, keeping the extension
            shutil.copy(source, destination)
            print(f"Copied {file_name} to {destination_path}")
            break  # Exit the loop once a match is found

print("Files have been copied successfully!")
