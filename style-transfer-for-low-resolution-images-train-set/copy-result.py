import os
import shutil

# Source and target directories
source_dir = 'Real-ESRGAN/result/filter-frame8-similarity-groups'
target_dir = 'style-transfer/origin-of-filter-frame8-similarity-groups'

# Check if source directory exists
if not os.path.exists(source_dir):
    print(f"Source directory {source_dir} does not exist.")
else:
    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Copy all files from source to target directory
    for filename in os.listdir(source_dir):
        source_file_path = os.path.join(source_dir, filename)
        target_file_path = os.path.join(target_dir, filename)
        
        try:
            shutil.copy2(source_file_path, target_file_path)
            print(f"Copied {filename}")
        except Exception as e:
            print(f"Could not copy {filename}. Error: {e}")

print("Copying process completed.")
