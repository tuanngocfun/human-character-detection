import os
import shutil

# Define paths
dir1 = "/media/ngoc/a normal usb/ngoc/training-set/super-resolution-similarity-images/kaggle/working/Real-ESRGAN/result/merge-cartoon-anime-low-quality-similarity-groups"
dir2 = "/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/merge-anime-cartoon-similarity-groups"
target_dir = "/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/refine/merge-anime-cartoon-similarity-groups"

# Create target directory if it does not exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# List files in each directory
files1 = os.listdir(dir1)
files2 = os.listdir(dir2)

# Strip "_out" and extension from names in dir1 for matching
files1_stripped = [f[:-8] for f in files1 if f.endswith("_out.jpg")]

# Strip extension from names in dir2 for matching
files2_stripped = [f[:-4] for f in files2 if f.endswith(".jpg")]

# Find matching files
matching_files = set(files1_stripped).intersection(files2_stripped)

# Copy matching files from dir1 to target directory
for match in matching_files:
    file_to_copy = match + "_out.jpg"
    shutil.copy(os.path.join(dir1, file_to_copy), os.path.join(target_dir, file_to_copy))

# Find non-matching files in dir2
non_matching_files = set(files2_stripped) - matching_files

# Copy non-matching files from dir2 to target directory
for non_match in non_matching_files:
    file_to_copy = non_match + ".jpg"
    shutil.copy(os.path.join(dir2, file_to_copy), os.path.join(target_dir, file_to_copy))

print(f"Finished copying matching and non-matching files to {target_dir}")