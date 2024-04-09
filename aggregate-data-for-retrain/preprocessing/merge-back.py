import os
import shutil

dest_dir = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction/merge-anime'

src_dir = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction/merge-cartoon-split'

def merge_back(src, dest):
    # Ensure the destination directory exists
    if not os.path.exists(dest):
        os.makedirs(dest)

    # Iterate through sub-directories in the source directory
    for subdir, _, files in os.walk(src):
        for file in files:
            # Build the full path to the source file and the destination file
            src_file_path = os.path.join(subdir, file)
            dest_file_path = os.path.join(dest, file)

            shutil.move(src_file_path, dest_file_path)

# Call the function
merge_back(src_dir, dest_dir)
