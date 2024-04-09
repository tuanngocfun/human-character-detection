import os
import shutil
import re

def copy_jpg_files(src_folder, target_folder):
    # Create target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Compile regex patterns for folder names
    pattern1 = re.compile(r'merge-filter-cartoon-frame-for-train\d+')
    pattern2 = re.compile(r'merge-filter-cartoon-frame-for-train\d+-similarity-groups')

    # Walk through the directory
    for root, dirs, files in os.walk(src_folder):
        # Check if the folder name matches the patterns
        if pattern1.match(os.path.basename(root)) or pattern2.match(os.path.basename(root)):
            for file in files:
                if file.endswith('.jpg'):
                    # Construct file paths
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(target_folder, file)
                    # Copy file
                    shutil.copy(src_file, dst_file)
                    print(f"Copied {src_file} to {dst_file}")

# Define source and target directories
src_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon'
target_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon/cp-all-merge-cartoon'

# Copy .jpg files from source to target directory
copy_jpg_files(src_dir, target_dir)

