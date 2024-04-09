import os
import shutil

def copy_matching_pairs(image_dir, label_dir, target_image_dir, target_label_dir):
    # Create the target directories if they don't exist
    os.makedirs(target_image_dir, exist_ok=True)
    os.makedirs(target_label_dir, exist_ok=True)

    # Iterate through the label files and look for corresponding image files
    for label_file in os.listdir(label_dir):
        if label_file.endswith('.txt'):
            image_file = label_file[:-4] + '.jpg'

            # Define source and target paths
            src_image_file = os.path.join(image_dir, image_file)
            src_label_file = os.path.join(label_dir, label_file)
            target_image_file = os.path.join(target_image_dir, image_file)
            target_label_file = os.path.join(target_label_dir, label_file)

            # Check if both the image and label files exist, and if not already in the target directory
            if os.path.exists(src_image_file) and os.path.exists(src_label_file):
                if not os.path.exists(target_image_file):
                    shutil.copy(src_image_file, target_image_file)
                if not os.path.exists(target_label_file):
                    shutil.copy(src_label_file, target_label_file)

# Paths to the old directories (source)
image_dir = '/media/ngoc/a normal usb/ngoc/test-set2/extract-frame-combine'
label_dir = '/media/ngoc/a normal usb/ngoc/thesis/ultralytics/runs/detect/predict10/labels'

# Paths to the new directories (target)
new_train_image_dir = '/media/ngoc/a normal usb/ngoc/test-set2/refine/images'
new_train_label_dir = '/media/ngoc/a normal usb/ngoc/test-set2/refine/labels'

# Copy the corresponding pairs of image and label files
copy_matching_pairs(image_dir, label_dir, new_train_image_dir, new_train_label_dir)

print('Files have been copied successfully.')
