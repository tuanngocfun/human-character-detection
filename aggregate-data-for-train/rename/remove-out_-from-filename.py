import os

# Define the path to the images and labels directories
images_dir = '/home/aivn12s2/data/upscale-dataset/images'
labels_dir = '/home/aivn12s2/data/upscale-dataset/labels'

# Function to remove '_out' from filenames in a directory
def rename_files_in_directory(dir_path, file_extension):
    # List all files in the directory
    for filename in os.listdir(dir_path):
        if '_out' in filename:
            # Create the new file name by replacing '_out' with an empty string
            new_filename = filename.replace('_out', '')
            # Rename the file
            os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))
            print(f"Renamed '{filename}' to '{new_filename}'")

            # Check for the corresponding label file if we're in the images directory
            if dir_path == images_dir:
                label_filename = filename.replace(file_extension, '.txt')
                new_label_filename = new_filename.replace(file_extension, '.txt')
                label_path = os.path.join(labels_dir, label_filename)
                new_label_path = os.path.join(labels_dir, new_label_filename)
                if os.path.exists(label_path):
                    # Rename the corresponding label file
                    os.rename(label_path, new_label_path)
                    print(f"Renamed label '{label_filename}' to '{new_label_filename}'")

# Rename files in images directory
rename_files_in_directory(images_dir, '.jpg')
# Rename files in labels directory (only if label files also contain '_out' in their names)
rename_files_in_directory(labels_dir, '.txt')

print("All files have been renamed.")
