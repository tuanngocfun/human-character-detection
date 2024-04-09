import os
import shutil

# Define the root directory where all the pattern folders and target folder exist
root_directory = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon'
target_directory = os.path.join(root_directory, 're-combine-cartoon')

# Ensure target directory exists
if not os.path.exists(target_directory):
    os.mkdir(target_directory)

# Define the patterns (which are now directories)
patterns = [f'filter-cartoon-frame{i}' for i in range(1, 7)]

# Iterate through the directories matching the patterns
for pattern in patterns:
    pattern_directory = os.path.join(root_directory, pattern)
    
    # Ensure the directory exists before proceeding
    if os.path.exists(pattern_directory):
        # Iterate through the files in the directory
        for filename in os.listdir(pattern_directory):
            file_path = os.path.join(pattern_directory, filename)
            if os.path.isfile(file_path):
                shutil.copy(file_path, target_directory)

print(f"All files from directories matching the patterns have been moved to {target_directory}")
