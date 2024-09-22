import os
import shutil
import re
import sys

# Ensure we get the correct number of arguments
if len(sys.argv) < 4:
    print("Usage: python photo_selector.py <path_to_all_photos> <destination_path> <file_names>")
    sys.exit(1)

# Arguments from command line
file_path_all_photos = sys.argv[1]
destination_path = sys.argv[2]
file_names_to_select = sys.argv[3:]

# Extract only the numeric parts of the input
file_numbers_to_select = [re.findall(r'\d+', name)[0] for name in file_names_to_select if re.findall(r'\d+', name)]

# Output the numbers from the input, separated by commas
print(f"Numbers from input: {', '.join(file_numbers_to_select)}")

# Ensure the destination directory exists
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

# Copy the files
for file_name in os.listdir(file_path_all_photos):
    # Extract the numeric part of the current file name
    file_number = re.findall(r'\d+', file_name)
    
    # If the file contains a number and it's in the list of numbers to select, copy it
    if file_number and file_number[0] in file_numbers_to_select:
        source = os.path.join(file_path_all_photos, file_name)
        destination = os.path.join(destination_path, file_name)
        
        # Copy the file
        shutil.copy(source, destination)
        print(f"Copied {file_name} to {destination_path}")

print("Files have been copied successfully!")
