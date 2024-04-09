import os
import shutil

def copy_files(src_base_dir, dest_dir, max_images_per_dir):
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    part_number = 1
    while True:
        # Formulate the source directory path based on the part number
        src_dir = os.path.join(src_base_dir, f'extract-frame-part{part_number}')
        # Break out of the loop if the source directory does not exist
        if not os.path.exists(src_dir):
            break

        images = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
        for image in images:
            src_path = os.path.join(src_dir, image)
            dest_path = os.path.join(dest_dir, image)
            shutil.copy2(src_path, dest_path)  # copy2 preserves file metadata

        part_number += 1

# Define the source base directory and destination directory
src_base_dir = '/media/ngoc/a normal usb/ngoc/test-set/'
dest_dir = '/media/ngoc/a normal usb/ngoc/test-set/extract-frame-refine'

# Call the function
copy_files(src_base_dir, dest_dir, 4000)

