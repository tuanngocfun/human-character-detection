import os

# Define the path to the directories
images_dir_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/add-filter-fram7-to-upscale-low-pixel-train/images'
labels_dir_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/add-filter-fram7-to-upscale-low-pixel-train/labels'

def rename_files(directory_path, file_extension):
    # List all files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file has the correct extension
        if filename.endswith(file_extension):
            # Extract the current file name without extension
            base_name = os.path.splitext(filename)[0]
            
            # Add 39857 to the existing file name
            new_base_name = str(int(base_name) + 39857)
            
            # Create new file name with the extension
            new_filename = new_base_name + file_extension
            
            # Full path to the existing and new file
            existing_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(directory_path, new_filename)
            
            # Rename the file
            os.rename(existing_file_path, new_file_path)
            print(f"Renamed {existing_file_path} to {new_file_path}")

# Rename jpg images
rename_files(images_dir_path, '.jpg')

# Rename txt labels
rename_files(labels_dir_path, '.txt')

