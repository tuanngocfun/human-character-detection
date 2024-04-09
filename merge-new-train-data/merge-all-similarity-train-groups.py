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
    '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon/filter-cartoon-frame1-similarity-groups',
    '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon/filter-cartoon-frame2-similarity-groups',
]

# Destination directory
destination_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon/merge-filter-cartoon-frame-for-train1'

copy_jpg_files(source_dirs, destination_dir)

print(f"Files from {', '.join(source_dirs)} have been merged into {destination_dir}")
