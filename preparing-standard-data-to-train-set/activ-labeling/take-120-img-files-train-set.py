import os
import re
import shutil

def get_image_order(filename):
    # Extract the numerical part of the filename using regex
    match = re.search(r'\d{5}', filename)
    if match:
        return int(match.group())
    return -1  # Return -1 if the numerical part is not found

# Directory containing the images and labels
image_dir = "/media/ngoc/a normal usb/ngoc/training-set/150th/images"

# Destination directory for the copied files
dest_dir = "/media/ngoc/a normal usb/ngoc/training-set/data/train-with120img"

# Create subdirectories for images and labels
image_dest_dir = os.path.join(dest_dir, 'images')
label_dest_dir = os.path.join(dest_dir, 'labels')

os.makedirs(image_dest_dir, exist_ok=True)
os.makedirs(label_dest_dir, exist_ok=True)

# List all files in the directory
all_files = os.listdir(image_dir)

# Filter only the .jpg and .txt files
jpg_files = [f for f in all_files if f.endswith('.jpg')]
txt_files = [f for f in all_files if f.endswith('.txt')]

# Sort the jpg files based on their numerical part
sorted_jpg_files = sorted(jpg_files, key=get_image_order)

# Take the first 120 jpg files and find their corresponding txt files
selected_jpg_files = sorted_jpg_files[:120]
selected_txt_files = [f.replace('.jpg', '.txt') for f in selected_jpg_files]

# Check if all corresponding txt files exist
for txt in selected_txt_files:
    if txt not in txt_files:
        print(f"Warning: Label file {txt} not found.")

# Now, copy the selected files to the respective destination subdirectories
for jpg, txt in zip(selected_jpg_files, selected_txt_files):
    shutil.copy(os.path.join(image_dir, jpg), os.path.join(image_dest_dir, jpg))
    if os.path.exists(os.path.join(image_dir, txt)):
        shutil.copy(os.path.join(image_dir, txt), os.path.join(label_dest_dir, txt))
