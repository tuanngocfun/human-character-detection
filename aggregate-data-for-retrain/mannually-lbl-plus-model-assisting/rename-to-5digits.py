import os
import re

# Define the directories containing the images and labels
images_directory = '/home/aivn12s2/data/train-set-without-upscale/activ-labeling-120-upscale-low-pixel/images'
labels_directory = '/home/aivn12s2/data/train-set-without-upscale/activ-labeling-120-upscale-low-pixel/labels'

# Define a function to rename files in a directory based on the provided pattern
def rename_files(directory, file_extension):
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):  # Check if the file has the correct file extension
            # Use regular expressions to replace 'data{number}_' pattern
            new_filename = re.sub(r'data\d+_', '', filename)
            # Get the full file paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the files
            os.rename(old_file, new_file)
            print(f"Renamed {filename} to {new_filename}")

# Rename .jpg files in the images directory
rename_files(images_directory, '.jpg')
# Rename .txt files in the labels directory
rename_files(labels_directory, '.txt')

print("All file renaming is complete.")
