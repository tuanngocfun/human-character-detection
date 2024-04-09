import os
import shutil

source_directory = "/home/aivn12s2/Downloads/upscale"
target_directory = "/home/aivn12s2/Downloads/upscale-all-in-one"

if not os.path.exists(target_directory):
    os.makedirs(target_directory)

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

for sub_dir in subdirectories:
    sub_dir_path = os.path.join(source_directory, sub_dir)

    if os.path.exists(sub_dir_path):

        for filename in os.listdir(sub_dir_path):

            if filename.endswith(".jpg"):
                file_path = os.path.join(sub_dir_path, filename)
                target_path = os.path.join(target_directory, filename)

                count = 1
                while os.path.exists(target_path):
                    name, ext = os.path.splitext(filename)
                    target_path = os.path.join(target_directory, f"{name}_{count}{ext}")
                    count += 1

                shutil.Copy(file_path, target_path)

print("All .jpg files have been copied to:", target_directory)

