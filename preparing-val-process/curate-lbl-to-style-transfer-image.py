import os
import shutil

# Source directory for label files
source_dir = '/media/ngoc/a normal usb/ngoc/new-val/val5-standard/labels'

# Target directory for copied and renamed label files
target_dir = '/media/ngoc/a normal usb/ngoc/new-val/labelimage3/curate-lbl-to-style-transfer-image'

# Create target directory if it does not exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Iterate through each file in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith('.txt'):
        
        # Append '_out' right before '.txt' in the file name
        new_filename = filename.replace('.txt', '_out.txt')
        
        # Full path to the file in the source directory
        source_file_path = os.path.join(source_dir, filename)
        
        # Full path to the renamed file in the target directory
        target_file_path = os.path.join(target_dir, new_filename)
        
        # Copy and rename the file to the target directory
        shutil.copy(source_file_path, target_file_path)
        print(f"Copied and renamed {filename} to {new_filename}")

print("All files have been copied and renamed successfully.")

