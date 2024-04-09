import os
import re

# Define the path to the images and labels directories
images_dir = '/home/aivn12s2/data/activ-labeling-120-upscale-low-pixel/images'
labels_dir = '/home/aivn12s2/data/activ-labeling-120-upscale-low-pixel/labels'

# List all files in the images directory
image_files = os.listdir(images_dir)
label_files = os.listdir(labels_dir)

# Regular expression pattern to match 'data<number>_' in the filenames
pattern = re.compile(r'data\d+_')

for image_file in image_files:
    # Check if the file name matches the pattern
    if pattern.match(image_file):
        # Create the new file name by substituting the matched pattern with an empty string
        new_image_name = pattern.sub('', image_file)
        # Rename the image file
        os.rename(os.path.join(images_dir, image_file), os.path.join(images_dir, new_image_name))

        # Assuming the label file has the same name before the extension
        label_file = image_file.replace('.jpg', '.txt')
        if label_file in label_files:
            new_label_name = new_image_name.replace('.jpg', '.txt')
            # Rename the label file
            os.rename(os.path.join(labels_dir, label_file), os.path.join(labels_dir, new_label_name))

print("Renaming completed.")
