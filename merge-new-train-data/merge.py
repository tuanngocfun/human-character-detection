import os
import shutil

# Function to merge two directories
def merge_directories(src1, src2, dest):
    # Check if the source directories exist
    if not os.path.exists(src1) or not os.path.exists(src2):
        print("One or both source directories do not exist.")
        return

    # Create destination directory if it doesn't exist
    if not os.path.exists(dest):
        os.makedirs(dest)

    # Copy jpg files from first source directory to destination
    for filename in os.listdir(src1):
        if filename.endswith('.jpg'):
            shutil.copy(os.path.join(src1, filename), os.path.join(dest, filename))

    # Copy jpg files from second source directory to destination
    for filename in os.listdir(src2):
        if filename.endswith('.jpg'):
            shutil.copy(os.path.join(src2, filename), os.path.join(dest, filename))

# Source directories
# src1 = 'filter-frame23'
# src2 = 'style-transfer/origin-of-filter-frame24'
src1 = 'filter-frame23'
src2 = 'filter-frame24'

# Destination directory
dest = 'adding-train-data-7-raw'

# Perform the merge
merge_directories(src1, src2, dest)
