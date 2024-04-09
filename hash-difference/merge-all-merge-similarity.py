import os
import shutil

def copy_jpg_files_from_dirs(src_dirs, target_dir):
    # Create target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for src_dir in src_dirs:
        # Check if the source directory exists
        if not os.path.exists(src_dir):
            print(f"Source directory does not exist: {src_dir}")
            continue

        # Walk through the source directory
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                if file.endswith('.jpg'):
                    # Construct the full file paths
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(target_dir, file)

                    # Copy file to target directory
                    shutil.copy(src_file, dst_file)
                    print(f"Copied {src_file} to {dst_file}")

# Define source directories
src_dirs = [
    '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-anime/cp-all-merge-anime',
    '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon/cp-all-merge-cartoon'
]

# Define target directory
target_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/dataset-of-hash-difference-first-time-merge-similarity'

# Copy .jpg files from source directories to the target directory
copy_jpg_files_from_dirs(src_dirs, target_dir)

