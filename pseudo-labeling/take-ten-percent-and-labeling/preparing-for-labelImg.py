import shutil
import os
import glob

def copy_files(src_path, target_path, file_extension):
    # Check if the source path exists
    if not os.path.exists(src_path):
        print(f"Error: Source path {src_path} does not exist.")
        return
    
    # Check if the target path exists, if not create it
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    
    # Construct the search pattern for the files
    search_pattern = os.path.join(src_path, f"*{file_extension}")
    
    # Find all files with the specified extension in the source path
    files_to_copy = glob.glob(search_pattern)
    
    # Copy each file to the target path
    for file_path in files_to_copy:
        shutil.copy(file_path, target_path)
        print(f"File {os.path.basename(file_path)} copied successfully to {target_path}")

# Define the source and target paths
image_src_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/pseudo-labeling-train-dataset-raw-images/images'
label_src_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/pseudo-labeling-train-dataset-raw-images/labels'
classes_src_path = '/media/ngoc/a normal usb/ngoc/training-set/150th/classes.txt'
target_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/activ-labeling-train-dataset-raw-images'

# Copy .jpg image files
copy_files(image_src_path, target_path, '.jpg')

# Copy .txt label files
copy_files(label_src_path, target_path, '.txt')

# Copy classes.txt file
if os.path.exists(classes_src_path):
    shutil.copy(classes_src_path, target_path)
    print(f"File classes.txt copied successfully to {target_path}")
else:
    print("Error: classes.txt source path does not exist.")

