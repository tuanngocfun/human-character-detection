import os

images_dir_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/add-filter-fram7-to-upscale-low-pixel-train/images'
labels_dir_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/add-filter-fram7-to-upscale-low-pixel-train/labels'

def rename_files(directory_path, file_extension):
    for filename in os.listdir(directory_path):
        if filename.endswith(file_extension):
            base_name = os.path.splitext(filename)[0]
            
            new_base_name = str(int(base_name) + 39857)
            
            new_filename = new_base_name + file_extension
            
            existing_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(directory_path, new_filename)
            
            os.rename(existing_file_path, new_file_path)
            print(f"Renamed {existing_file_path} to {new_file_path}")

rename_files(images_dir_path, '.jpg')

rename_files(labels_dir_path, '.txt')

