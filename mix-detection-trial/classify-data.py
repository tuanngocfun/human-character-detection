import os
import shutil

# Define paths
label_path = '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict63/labels'
image_path = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate3/images'
target_path = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/not-labeled-by-first-detect/human-real-world-detect-here'

# Create target directory if it doesn't exist
if not os.path.exists(target_path):
    os.makedirs(target_path)

# Fetch all label files
label_files = set([f for f in os.listdir(label_path) if f.endswith('.txt')])

# Loop through each .jpg file in the image directory
for image_file in os.listdir(image_path):
    if image_file.endswith('.jpg'):
        # Create a corresponding label filename
        label_file = image_file.replace('.jpg', '.txt')
        
        # Check if the corresponding label file exists
        if label_file not in label_files:
            # Copy the .jpg file to the target directory
            src = os.path.join(image_path, image_file)
            dest = os.path.join(target_path, image_file)
            shutil.copy(src, dest)
            print(f"Copied {image_file} to {target_path}")