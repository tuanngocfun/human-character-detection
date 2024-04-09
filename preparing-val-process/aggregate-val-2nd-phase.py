import shutil
import os

def copy_subdirectories(subdir_name, destination_path):
    base_path = "/media/ngoc/a normal usb/ngoc/new-val"
    source_dirs = ["valid-refirst-phase", "val5-style-transfer"]

    # Ensure the destination directory exists
    os.makedirs(destination_path, exist_ok=True)

    for src_dir in source_dirs:
        # Construct the full path to the source subdirectory
        src_subdir_path = os.path.join(base_path, src_dir, subdir_name)
        
        # Copy all contents from the source subdirectory to the destination
        for item in os.listdir(src_subdir_path):
            src_item_path = os.path.join(src_subdir_path, item)
            dest_item_path = os.path.join(destination_path, item)
            if os.path.isdir(src_item_path):
                shutil.copytree(src_item_path, dest_item_path)
            else:
                shutil.copy2(src_item_path, dest_item_path)

# Path for "valid-first-phase"
valid_second_phase_path = "/media/ngoc/a normal usb/ngoc/new-val/valid-second-phase-with-val5-style-transfer"

# Copy images subdirectory
copy_subdirectories("images", os.path.join(valid_second_phase_path, "images"))

# Copy labels subdirectory
copy_subdirectories("labels", os.path.join(valid_second_phase_path, "labels"))
