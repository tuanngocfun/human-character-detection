import os
import shutil
import random

# Source and target directories
source_dir = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/train-dataset-raw-images'
target_dir = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/pseudo-labeling-train-dataset-raw-images'

# Subdirectories for images and labels
image_subdir = 'images'
label_subdir = 'labels'

# Full paths for source and target image and label directories
source_image_dir = os.path.join(source_dir, image_subdir)
source_label_dir = os.path.join(source_dir, label_subdir)
target_image_dir = os.path.join(target_dir, image_subdir)
target_label_dir = os.path.join(target_dir, label_subdir)

# Create target directories if they don't exist
os.makedirs(target_image_dir, exist_ok=True)
os.makedirs(target_label_dir, exist_ok=True)

# List all .jpg and .txt files
image_files = [f for f in os.listdir(source_image_dir) if f.endswith('.jpg')]
label_files = set([f for f in os.listdir(source_label_dir) if f.endswith('.txt')]) # Using set for faster lookup

# Calculate 10% of the total number of image files
num_files_to_copy = int(len(image_files) * 0.0155)

# Randomly select image files
selected_image_files = random.sample(image_files, num_files_to_copy)

# Copy selected image and corresponding label files
for image_file in selected_image_files:
    # Construct full path for source and target image files
    source_image_path = os.path.join(source_image_dir, image_file)
    target_image_path = os.path.join(target_image_dir, image_file)
    
    # Copy image file
    shutil.copy(source_image_path, target_image_path)

    # Construct the corresponding label file name and its full paths
    label_file = image_file.rsplit('.', 1)[0] + '.txt'
    source_label_path = os.path.join(source_label_dir, label_file)
    target_label_path = os.path.join(target_label_dir, label_file)

    # Check if the corresponding label file exists in the source directory
    if label_file in label_files:
        # Copy label file
        shutil.copy(source_label_path, target_label_path)
    else:
        print(f"Warning: Corresponding label file {label_file} not found.")

print(f"Copied {num_files_to_copy} image files and their corresponding label files.")

