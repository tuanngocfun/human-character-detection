import os
import shutil
import random

# Define the paths
source_images_path = '/home/aivn12s2/data/final-test-set/images'
source_labels_path = '/home/aivn12s2/data/final-test-set/labels'
target_path = '/home/aivn12s2/data/val-data-1541-from-test-set'
target_images_path = os.path.join(target_path, 'images')
target_labels_path = os.path.join(target_path, 'labels')

# Ensure target directories exist
os.makedirs(target_images_path, exist_ok=True)
os.makedirs(target_labels_path, exist_ok=True)

# Get a list of label files
label_files = [f for f in os.listdir(source_labels_path) if f.endswith('.txt')]
# Select 1541 unique label files randomly
selected_labels = random.sample(label_files, 1541)

# Copy the selected label and corresponding image files to the target directories
for label_file in selected_labels:
    # Construct full paths to the source files
    source_label_path = os.path.join(source_labels_path, label_file)
    # Images have the same name as the label files, but with .jpg extension
    image_file = label_file.replace('.txt', '.jpg')
    source_image_path = os.path.join(source_images_path, image_file)

    # Construct full paths to the target files
    target_label_path = os.path.join(target_labels_path, label_file)
    target_image_path = os.path.join(target_images_path, image_file)

    # Check if the image file exists to ensure there is a corresponding image for the label
    if os.path.exists(source_image_path):
        # Copy the files
        shutil.copy2(source_label_path, target_label_path)
        shutil.copy2(source_image_path, target_image_path)
    else:
        print(f"Image file does not exist for {label_file}")

print("Files successfully copied.")
