import os
import re

def clean_filename(filename):
    """
    Remove forbidden characters from the filename.
    """
    # Remove square brackets and ampersand
    cleaned_name = re.sub(r'[\[\]&]', '', filename)
    return cleaned_name

def rename_files_in_directory(folder_path, img_dir='images', lbl_dir='labels'):
    """
    Rename files in the given directory and its sub-directory.
    
    Parameters:
        folder_path: str - path to the parent folder
        img_dir: str - name of the image directory
        lbl_dir: str - name of the label directory
    """
    # Full paths to the image and label directories
    image_folder = os.path.join(folder_path, img_dir)
    label_folder = os.path.join(folder_path, lbl_dir)

    for dirpath, _, filenames in os.walk(image_folder):
        for filename in filenames:
            if filename.endswith('.jpg'):
                # Construct old and new file paths for image
                old_image_path = os.path.join(dirpath, filename)
                new_image_name = clean_filename(filename)
                new_image_path = os.path.join(dirpath, new_image_name)
                
                # Construct old and new file paths for label
                old_label_name = filename.replace('.jpg', '.txt')
                new_label_name = new_image_name.replace('.jpg', '.txt')
                old_label_path = os.path.join(label_folder, old_label_name)
                new_label_path = os.path.join(label_folder, new_label_name)
                
                # Rename image and label files
                os.rename(old_image_path, new_image_path)
                if os.path.exists(old_label_path):
                    os.rename(old_label_path, new_label_path)
                print(f"Renamed {old_image_path} to {new_image_path}")
                print(f"Renamed {old_label_path} to {new_label_path}")

#folder_path = '/media/ngoc/mydisk/ngoc/thesis/dataset/aggregate4'
folder_path = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon/combine-cartoon'
rename_files_in_directory(folder_path)

