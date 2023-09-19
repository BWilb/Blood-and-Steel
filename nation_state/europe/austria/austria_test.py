import os
import json

# Get the current directory of file1.py
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the JSON file
relative_path_to_json = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'

# Construct the full path to the JSON file
json_file_path = os.path.normpath(os.path.join(current_directory, relative_path_to_json))
print(json_file_path)

# Check if the file exists
if os.path.exists(json_file_path):
    # Open and read the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        # Now, 'data' contains the JSON content
        print(data)
else:
    print(f"The file 'data.json' does not exist in the specified folder.")
