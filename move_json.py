import os
import shutil

# Specify the source directory where the JSON files are located
src_dir = './'

# Specify the destination directory where the JSON files will be moved
dest_dir = './json/'

# Walk through the source directory and its subdirectories
for root, dirs, files in os.walk(src_dir):
    # Loop through all the files in the current directory
    for file in files:
        # Check if the file is a JSON file
        if file.endswith('.json'):
            # Get the relative path of the file with respect to the source directory
            rel_path = os.path.relpath(os.path.join(root, file), src_dir)
            # Construct the destination directory for the file
            dest_path = os.path.join(dest_dir, rel_path)
            # Create the destination directory if it doesn't exist
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            # Move the file to the destination directory
            shutil.move(os.path.join(root, file), dest_path)