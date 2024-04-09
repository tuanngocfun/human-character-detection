import os
import shutil
from glob import glob

def filter_and_copy_files(image_dir, label_dir, dest_dir):
    dest_image_dir = os.path.join(dest_dir, 'images')
    dest_label_dir = os.path.join(dest_dir, 'labels')
    os.makedirs(dest_image_dir, exist_ok=True)
    os.makedirs(dest_label_dir, exist_ok=True)

    # List all image and label files
    image_files = glob(os.path.join(image_dir, '*.jpg')) 
    label_files = glob(os.path.join(label_dir, '*.txt'))  

    # Filter image files that have corresponding label files
    filtered_image_files = [
        os.path.join(image_dir, os.path.basename(label_file).replace('.txt', '.jpg'))
        for label_file in label_files
        if os.path.exists(os.path.join(image_dir, os.path.basename(label_file).replace('.txt', '.jpg')))
    ]

    # Copy filtered image and label files to new directories
    for image_file in filtered_image_files:
        shutil.copy(image_file, dest_image_dir)

    for label_file in label_files:
        label_file_name = os.path.basename(label_file)
        corresponding_image_file_name = label_file_name.replace('.txt', '.jpg')
        
        if corresponding_image_file_name in [os.path.basename(img) for img in filtered_image_files]:
            shutil.copy(label_file, dest_label_dir)

    print("Filtered and copied image and label files.")

# Source directories
image_dir = '/media/ngoc/a normal usb/ngoc/training-set/aggregate4/images'
label_dir = '/media/ngoc/a normal usb/ngoc/thesis/ultralytics/runs/detect/predict9/labels'

# Destination directory
dest_dir = '/media/ngoc/a normal usb/ngoc/training-set/aggregate4-retrain/'

filter_and_copy_files(image_dir, label_dir, dest_dir)
