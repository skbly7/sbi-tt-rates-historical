import os
import json

# Set the paths for the input and output directories
input_dir = 'json/'
output_dir = 'json/'

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.json') and not filename.startswith('v2_'):
        # Open the input file and load the original records
        with open(os.path.join(input_dir, filename)) as f:
            original_records = json.load(f)

        # Create an empty dictionary to store the new records
        new_records = {}

        # Loop through each record in the original list and convert it to the new format
        for record in original_records:
            symbol = record['SYMBOL']
            values = {k: v for k, v in record.items() if k != 'SYMBOL'}
            new_records[symbol] = values

        # Write the new dictionary to a file in the output directory in JSON format
        with open(os.path.join(output_dir, f'v2_{filename}'), 'w') as f:
            json.dump(new_records, f)
