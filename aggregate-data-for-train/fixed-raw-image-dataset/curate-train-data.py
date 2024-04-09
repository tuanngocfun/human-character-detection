import os
import shutil

# Define the source and target directories
source_dir = '/home/aivn12s2/data/train-set-without-upscale/aggregate4-raw-quality-with-fixed-manually-lbl'
target_dir = '/home/aivn12s2/data/train-set-without-upscale/aggregate4-raw-quality-with-fixed-manually-lbl-fixed'

# Create target directory structure
if not os.path.exists(target_dir):
    shutil.copytree(source_dir, target_dir)

# Define paths to the image and label subdirectories
images_src_dir = os.path.join(source_dir, 'images')
images_target_dir = os.path.join(target_dir, 'images')
labels_src_dir = os.path.join(source_dir, 'labels')
labels_target_dir = os.path.join(target_dir, 'labels')

# Function to handle the prioritization and renaming of files
def handle_file_priority(subdir, extension):
    # List all files in the source subdirectory
    for file in os.listdir(subdir):
        if file.endswith(extension):
            base_name = file.split('.')[0]
            # Check if the prioritized version exists (e.g., with '_out')
            if base_name.endswith('_out'):
                normal_file = base_name[:-4] + extension
                prioritized_file = file

                # Check if both versions exist
                if os.path.exists(os.path.join(subdir, normal_file)):
                    # Remove the non-prioritized file
                    os.remove(os.path.join(subdir, normal_file))

                # Rename the prioritized file to the standard name
                os.rename(os.path.join(subdir, prioritized_file),
                          os.path.join(subdir, normal_file))

# Process images
handle_file_priority(images_target_dir, '.jpg')

# Process labels
handle_file_priority(labels_target_dir, '.txt')

print("Processing complete.")
