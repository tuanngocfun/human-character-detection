import os
import re
import shutil
import random

def get_movie_name(filename):
    # Use regular expression to extract the movie name part
    match = re.search(r'^(.+?)_frame', filename)
    if match:
        return match.group(1)
    return None

# Source subdirectories containing the images and labels
image_src_dir = "/media/ngoc/a normal usb/ngoc/final-test-set/images"
label_src_dir = "/media/ngoc/a normal usb/ngoc/final-test-set/labels"

# Destination directory for the copied files
dest_dir = "/media/ngoc/a normal usb/ngoc/activ-learning-with-25-img-test"

# Create subdirectories for images and labels
image_dest_dir = os.path.join(dest_dir, 'images')
label_dest_dir = os.path.join(dest_dir, 'labels')

os.makedirs(image_dest_dir, exist_ok=True)
os.makedirs(label_dest_dir, exist_ok=True)

# List all files in the source subdirectories
jpg_files = os.listdir(image_src_dir)
txt_files = os.listdir(label_src_dir)

# Group jpg files by their movie names
movie_dict = {}
for jpg in jpg_files:
    movie_name = get_movie_name(jpg)
    if movie_name:
        if movie_name not in movie_dict:
            movie_dict[movie_name] = []
        movie_dict[movie_name].append(jpg)

# Randomly choose 25 jpg files, prefer to choose different movie names
selected_jpg_files = []
for movie in random.sample(list(movie_dict.keys()), min(25, len(movie_dict))):
    selected_jpg_files.append(random.choice(movie_dict[movie]))

# Find corresponding txt files
selected_txt_files = [f.replace('.jpg', '.txt') for f in selected_jpg_files]

# Check if all corresponding txt files exist
for txt in selected_txt_files:
    if txt not in txt_files:
        print(f"Warning: Label file {txt} not found.")

# Now, copy the selected files to the respective destination subdirectories
for jpg, txt in zip(selected_jpg_files, selected_txt_files):
    shutil.copy(os.path.join(image_src_dir, jpg), os.path.join(image_dest_dir, jpg))
    if os.path.exists(os.path.join(label_src_dir, txt)):
        shutil.copy(os.path.join(label_src_dir, txt), os.path.join(label_dest_dir, txt))
