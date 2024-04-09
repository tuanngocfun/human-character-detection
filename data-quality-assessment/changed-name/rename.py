import shutil
import os

# Define the source and target directories
source_dir = '/media/ngoc/a normal usb/ngoc/training-set/aggregate4/images'
target_dir = '/media/ngoc/a normal usb/ngoc/training-set/aggregate4-changed-name/images'

# Create the target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Copy all files from the source to the target directory
for filename in os.listdir(source_dir):
    source_path = os.path.join(source_dir, filename)
    target_path = os.path.join(target_dir, filename)
    if os.path.isfile(source_path):
        shutil.copy(source_path, target_path)

# Rename .jpg files in the target directory
jpg_files = [f for f in os.listdir(target_dir) if f.endswith('.jpg')]
for idx, filename in enumerate(sorted(jpg_files), start=0):
    old_path = os.path.join(target_dir, filename)
    new_name = f'{idx:04d}.jpg'
    new_path = os.path.join(target_dir, new_name)
    os.rename(old_path, new_path)

