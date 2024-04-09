import os
import shutil

def partition_images(src_dir, dest_base_dir, max_images_per_dir):
    if not os.path.exists(src_dir):
        raise ValueError(f"The source directory {src_dir} does not exist.")

    # Ensure the destination base directory exists
    os.makedirs(dest_base_dir, exist_ok=True)

    images = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
    total_images = len(images)

    part_number = 1
    for i in range(0, total_images, max_images_per_dir):
        # Create the new directory
        part_dir_name = f"extract-frame-part{part_number}"
        part_dir_path = os.path.join(dest_base_dir, part_dir_name)
        os.makedirs(part_dir_path, exist_ok=True)

        # Move the images to the new directory
        for j in range(i, min(i + max_images_per_dir, total_images)):
            src_path = os.path.join(src_dir, images[j])
            dest_path = os.path.join(part_dir_path, images[j])
            shutil.move(src_path, dest_path)

        part_number += 1

# Define the source and destination directories
src_dir = '/media/ngoc/a normal usb/ngoc/test-set2/extract-frame2'
dest_base_dir = '/media/ngoc/a normal usb/ngoc/test-set2/'

# Call the function
partition_images(src_dir, dest_base_dir, 4500)

