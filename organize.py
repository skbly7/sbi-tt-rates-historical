import os
import shutil
import sys

def main(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Loop through each file in the directory
    for file in files:
        if not file.endswith('pdf'):
            continue
        # Split the filename into its components
        parts = file.split('-')
        if len(parts) < 4:
            continue
        # Extract the year, month, day, hour, and minute from the filename
        year = parts[0]
        month = parts[1]
        day = parts[2]

        # Determine the separator between the hour and minute
        time_parts = parts[3].split(':')
        if len(time_parts) == 1:
            hour = time_parts[0][:2]
            minute = time_parts[0][2:]
        else:
            hour = time_parts[0]
            minute = time_parts[1]

        # Create the directory structure if it doesn't already exist
        if not os.path.exists(os.path.join(directory, year, month)):
            os.makedirs(os.path.join(directory, year, month))

        # Move the file to the appropriate directory
        shutil.move(os.path.join(directory, file), os.path.join(directory, year, month, file))

if __name__ == '__main__':
    # Get the input directory path from the command-line arguments
    if len(sys.argv) < 2:
        print('Usage: python organize.py <directory>')
        sys.exit(1)
    directory = sys.argv[1]

    # Call the main function with the input directory path
    main(directory)
