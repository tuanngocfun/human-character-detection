import shutil
import os
import glob

def copy_jpg_files(source_dirs, destination_dir):
    # Check if destination directory exists, if not, create it
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate through the source directories and copy jpg files
    for source_dir in source_dirs:
        if os.path.exists(source_dir):
            for jpg_file in glob.glob(f'{source_dir}/*.jpg'):
                shutil.copy(jpg_file, destination_dir)
        else:
            print(f"Source directory {source_dir} does not exist. Skipping...")

# List of directories to merge
source_dirs = [
    'filter-frame3-similarity-groups',
    'filter-frame4-similarity-groups',
    'filter-frame5-similarity-groups',
    'filter-frame5'
]

# Destination directory
destination_dir = 'merge-filter-frame-for-val'

copy_jpg_files(source_dirs, destination_dir)

print(f"Files from {', '.join(source_dirs)} have been merged into {destination_dir}")
