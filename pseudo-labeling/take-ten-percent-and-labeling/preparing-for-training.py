import os
import shutil

source_dir = "/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/activ-labeling-train-dataset-raw-images"
image_dest_dir = "/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/manually-labeling-for-pseudo-labeling-finish/images"
label_dest_dir = "/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/manually-labeling-for-pseudo-labeling-finish/labels"

# Create destination directories if they don't exist
os.makedirs(image_dest_dir, exist_ok=True)
os.makedirs(label_dest_dir, exist_ok=True)

# Iterate over files in the source directory
for filename in os.listdir(source_dir):
    filepath = os.path.join(source_dir, filename)
    
    # Process text files
    if filename.endswith('.txt') and filename != 'classes.txt':
        with open(filepath, 'r') as file:
            content = file.read().strip()
            
            # Only copy text files with content
            if content:
                label_dest_path = os.path.join(label_dest_dir, filename)
                shutil.copy(filepath, label_dest_path)
            
            # If text file is empty, find the corresponding image and skip copying it
            elif content == '':
                image_filename = filename.replace('.txt', '.jpg')
                continue

    # Process image files
    elif filename.endswith('.jpg'):
        # Check if corresponding text file exists and is not empty
        text_filename = filename.replace('.jpg', '.txt')
        text_filepath = os.path.join(source_dir, text_filename)
        if os.path.exists(text_filepath):
            with open(text_filepath, 'r') as text_file:
                text_content = text_file.read().strip()
                if text_content:
                    image_dest_path = os.path.join(image_dest_dir, filename)
                    shutil.copy(filepath, image_dest_path)

# Move 'classes.txt' file if exists
classes_txt_path = os.path.join(source_dir, 'classes.txt')
if os.path.exists(classes_txt_path):
    shutil.copy(classes_txt_path, "/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/manually-labeling-for-pseudo-labeling-finish/")

# Verify that each .txt label file has its own .jpg image file and vice versa
for filename in os.listdir(label_dest_dir):
    image_filename = filename.replace('.txt', '.jpg')
    if not os.path.exists(os.path.join(image_dest_dir, image_filename)):
        os.remove(os.path.join(label_dest_dir, filename))

for filename in os.listdir(image_dest_dir):
    text_filename = filename.replace('.jpg', '.txt')
    if not os.path.exists(os.path.join(label_dest_dir, text_filename)):
        os.remove(os.path.join(image_dest_dir, filename))
