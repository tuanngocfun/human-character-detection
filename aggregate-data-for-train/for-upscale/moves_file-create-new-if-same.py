import os
import shutil

# Source and target directories
source_directory = "/home/aivn12s2/Downloads/upscale"
target_directory = "/home/aivn12s2/Downloads/upscale-all-in-one"

# Create target directory if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Subdirectories based on the given information
subdirectories = [
    "merge-anime-cartoon",
    "super-resolution-anime-images_sub-dir1_1",
    "super-resolution-anime-images_sub-dir1_2",
    "super-resolution-anime-images_sub-dir1_3",
    "super-resolution-anime-images_sub-dir2",
    "super-resolution-anime-images_sub-dir3",
    "super-resolution-anime-images_sub-dir4",
    "super-resolution-cartoon-images_sub-dir1",
    "super-resolution-cartoon-images_sub-dir2"
]

# Iterate through each subdirectory
for sub_dir in subdirectories:
    sub_dir_path = os.path.join(source_directory, sub_dir)

    # Check if the subdirectory exists
    if os.path.exists(sub_dir_path):

        # Iterate through each file in the subdirectory
        for filename in os.listdir(sub_dir_path):

            # Check if the file is a .jpg file
            if filename.endswith(".jpg"):
                file_path = os.path.join(sub_dir_path, filename)
                target_path = os.path.join(target_directory, filename)

                # Check if a file with the same name exists in the target directory
                count = 1
                while os.path.exists(target_path):
                    name, ext = os.path.splitext(filename)
                    target_path = os.path.join(target_directory, f"{name}_{count}{ext}")
                    count += 1

                # Copy the .jpg file to the target directory
                shutil.Copy(file_path, target_path)

print("All .jpg files have been copied to:", target_directory)

