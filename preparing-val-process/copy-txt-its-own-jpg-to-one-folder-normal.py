import os
import shutil

# Source and target directories
label_src = '/media/ngoc/a normal usb/ngoc/new-val/labelimage3/curate-lbl-to-style-transfer-image/labels'
image_src = '/media/ngoc/a normal usb/ngoc/new-val/labelimage3/transfer-done-val5/images'
target_dir = '/media/ngoc/a normal usb/ngoc/new-val/labelimage3/lbl-img-style-transfer-normal'

# Create the target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Get a list of all .txt and .jpg files
label_files = [f for f in os.listdir(label_src) if f.endswith('.txt')]
image_files = [f for f in os.listdir(image_src) if f.endswith('.jpg')]

# Copying files with matching labels and images
for label in label_files:
    # Removing the extension to match the image file
    name_without_extension = os.path.splitext(label)[0]
    corresponding_image = name_without_extension + '.jpg'
    
    if corresponding_image in image_files:
        shutil.copy(os.path.join(label_src, label), os.path.join(target_dir, label))
        shutil.copy(os.path.join(image_src, corresponding_image), os.path.join(target_dir, corresponding_image))

# Second verification to ensure each .txt has a corresponding .jpg and vice versa
final_txt_files = [f for f in os.listdir(target_dir) if f.endswith('.txt')]
final_jpg_files = [f for f in os.listdir(target_dir) if f.endswith('.jpg')]

for label in final_txt_files:
    name_without_extension = os.path.splitext(label)[0]
    corresponding_image = name_without_extension + '.jpg'
    
    if corresponding_image not in final_jpg_files:
        os.remove(os.path.join(target_dir, label))

for image in final_jpg_files:
    name_without_extension = os.path.splitext(image)[0]
    corresponding_label = name_without_extension + '.txt'
    
    if corresponding_label not in final_txt_files:
        os.remove(os.path.join(target_dir, image))

print("Operation completed. The target directory now contains only matching .jpg and .txt files.")

