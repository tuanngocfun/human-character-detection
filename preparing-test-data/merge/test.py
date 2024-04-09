import os
import shutil
import re

def merge_directories(src_base_dir, dest_dir):
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    # Regular expression to match the desired pattern
    pattern = re.compile(r'^extract-frame-part\d+$')
    
    # List all directories in the source base directory that match the pattern
    dirs = [d for d in os.listdir(src_base_dir) if os.path.isdir(os.path.join(src_base_dir, d)) and pattern.match(d)]
    
    for dir_name in dirs:
        src_dir_path = os.path.join(src_base_dir, dir_name)
        for file_name in os.listdir(src_dir_path):
            src_file_path = os.path.join(src_dir_path, file_name)
            dest_file_path = os.path.join(dest_dir, file_name)
            
            # To prevent overwriting files with the same name, check if a file with the same name already exists in the destination directory
            counter = 1
            while os.path.exists(dest_file_path):
                name, ext = os.path.splitext(file_name)
                dest_file_path = os.path.join(dest_dir, f"{name}_{counter}{ext}")
                counter += 1
                
            shutil.copy(src_file_path, dest_file_path)

# Define the source base directory and destination directory
src_base_dir = '/media/ngoc/a normal usb/ngoc/test-set2/'
dest_dir = '/media/ngoc/a normal usb/ngoc/test-set2/extract-frame-combine'

# Call the function
merge_directories(src_base_dir, dest_dir)

