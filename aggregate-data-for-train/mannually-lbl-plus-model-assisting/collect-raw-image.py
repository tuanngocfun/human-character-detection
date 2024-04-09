import os
import shutil

def copy_with_priority(src_img_1, src_label_1, src_img_2, src_label_2, target_img, target_label):
    # Make sure target directories exist
    if not os.path.exists(target_img):
        os.makedirs(target_img)
    if not os.path.exists(target_label):
        os.makedirs(target_label)

    # Copy from first priority directory
    for filename in os.listdir(src_img_1):
        if filename.endswith(".jpg"):
            label_file = filename.replace(".jpg", ".txt")

            # Copy image file
            shutil.copy(os.path.join(src_img_1, filename), os.path.join(target_img, filename))

            # Copy corresponding label file
            shutil.copy(os.path.join(src_label_1, label_file), os.path.join(target_label, label_file))

    # Copy from second priority directory
    for filename in os.listdir(src_img_2):
        if filename.endswith(".jpg"):
            label_file = filename.replace(".jpg", ".txt")

            target_img_path = os.path.join(target_img, filename)
            target_label_path = os.path.join(target_label, label_file)

            # Check if the file already exists in the target directory (first priority)
            if not os.path.exists(target_img_path) and not os.path.exists(target_label_path):
                # Copy image file
                shutil.copy(os.path.join(src_img_2, filename), target_img_path)

                # Copy corresponding label file
                shutil.copy(os.path.join(src_label_2, label_file), target_label_path)

# Source directories for first priority
src_img_1 = '/home/aivn12s2/data/train-set-without-upscale/activ-labeling-120-upscale-low-pixel/images'
src_label_1 = '/home/aivn12s2/data/train-set-without-upscale/activ-labeling-120-upscale-low-pixel/labels'

# Source directories for second priority
src_img_2 = '/home/aivn12s2/data/train-set-without-upscale/images'
src_label_2 = '/home/aivn12s2/data/train-set-without-upscale/labels'

# Target directories
target_img = '/home/aivn12s2/data/train-set-without-upscale/aggregate4-raw-quality-with-fixed-manually-lbl/images'
target_label = '/home/aivn12s2/data/train-set-without-upscale/aggregate4-raw-quality-with-fixed-manually-lbl/labels'

copy_with_priority(src_img_1, src_label_1, src_img_2, src_label_2, target_img, target_label)
