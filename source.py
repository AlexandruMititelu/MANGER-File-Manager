import os
import shutil

COUNTER = 0

def is_valid_filename(file_path):
    # File can be a str that is either an int or a str that must contain at least one digit
    return file_path.isnumeric() or any(char.isdigit() for char in file_path)

def extract_numbers(file_name) -> str:
    # Extract digits from the file name
    return ''.join(filter(str.isdigit, file_name))


# Define the paths for the source and destination folders
file_path_all_photos = "D:\Photos 12\SRVU Board 2024 Sept"
destination_path = "D:\Photos 12\SRVU selected"

# Check if the source folder exists
if not os.path.exists(file_path_all_photos):
    print(f"Error: The path '{file_path_all_photos}' does not exist.")
    exit(1)


try:
    # Read the parts of the filenames or numbers to select from the 'input' file
    with open('input', 'r') as file:
        file_names_to_select = list(
            map(
                extract_numbers, 
                filter(is_valid_filename, file.readlines())
            )        
        )
except FileNotFoundError:
    print("Error: The 'input' file does not exist.")
    exit(1)
except Exception as e:
    print(f"An error occurred while reading the 'input' file: {e}")
    exit(1)

# Ensure the destination directory exists, create if it doesn't
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

try:
    # Copy the files that match the given patterns
    for file_name in os.listdir(file_path_all_photos):
        for pattern in file_names_to_select:
            if pattern in file_name:
                COUNTER += 1
                source = os.path.join(file_path_all_photos, file_name)
                destination = os.path.join(destination_path, file_name)

                # Copy the file, keeping the extension
                shutil.copy(source, destination)
                print(f"Copied {file_name} to {destination_path}")
                break  # Exit the loop once a match is found
except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"Files have been copied successfully! {COUNTER} photos have been selected")
