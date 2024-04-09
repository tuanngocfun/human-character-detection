import os
import re
import yaml

def find_yaml_with_path(search_directory, target_path):
    # Regex pattern to match '/train' and '/train{number}'
    train_dir_pattern = re.compile(r"^train(\d+)?$")
    
    # List to store the paths of 'args.yaml' files containing the specified text
    relevant_yaml_files = []

    # Walk through the directory
    for dirpath, dirnames, _ in os.walk(search_directory):
        # Filter out the directories that don't match our pattern
        filtered_dirs = [d for d in dirnames if train_dir_pattern.match(d)]

        for dirname in filtered_dirs:
            # Construct the path to the 'args.yaml' file
            args_path = os.path.join(dirpath, dirname, 'args.yaml')
            
            # Check if the 'args.yaml' file exists
            if os.path.isfile(args_path):
                # Read the 'args.yaml' file and search for the specific line
                try:
                    with open(args_path, 'r') as file:
                        data = yaml.safe_load(file)  # Load the YAML file safely
                        # Assuming the path we are looking for is in the YAML as a value
                        if target_path in str(data):
                            relevant_yaml_files.append(args_path)
                except Exception as e:
                    print(f"Error reading or parsing file {args_path}: {e}")

    return relevant_yaml_files

# Set the directory where to start the search
search_directory = '/home/aivn12s2/ultralytics/runs/detect'
# Set the target path we're looking for in the YAML files
target_path = '/home/aivn12s2/data/data-not-upscale.yaml'

# Use the function and print the results
found_files = find_yaml_with_path(search_directory, target_path)
for file in found_files:
    print(f"Found in: {file}")
