import os
import shutil
import re

# Define the source and target directories
source_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/cosine-similarity-extract/extract-cartoon'
target_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/cosine-similarity-extract/extract-cartoon/merge-cartoon'

# Make sure the target directory exists, if not, create it
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Compile a regular expression pattern for matching the directories
dir_pattern = re.compile(r'filter-cartoon-frame\d+')

# Walk through the source directory
for item in os.listdir(source_dir):
    item_path = os.path.join(source_dir, item)
    # Check if the item is a directory and matches the pattern
    if os.path.isdir(item_path) and dir_pattern.match(item):
        # Loop through each file in the subdirectory
        for filename in os.listdir(item_path):
            file_path = os.path.join(item_path, filename)
            # Check if it's a file and not a subdirectory
            if os.path.isfile(file_path):
                # Construct the full destination path
                dst_path = os.path.join(target_dir, filename)
                # In case a file with the same name already exists, append an incrementing number
                copy_number = 1
                while os.path.exists(dst_path):
                    base, extension = os.path.splitext(filename)
                    dst_path = os.path.join(target_dir, f"{base}_{copy_number}{extension}")
                    copy_number += 1
                # Copy the file
                shutil.copy2(file_path, dst_path)
                print(f"Copied {filename} to merge-cartoon directory")

print("All files have been copied.")
