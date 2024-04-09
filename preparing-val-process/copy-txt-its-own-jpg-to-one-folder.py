import os
import shutil

def copy_and_curate_files(src_image_dir, src_label_dir, target_dir):
    # Create target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Load all files in both directories
    src_image_files = [f for f in os.listdir(src_image_dir) if f.endswith('.jpg')]
    src_label_files = [f for f in os.listdir(src_label_dir) if f.endswith('.txt')]
    
    # Dictionary to keep track of copied files
    copied_files = {'image': [], 'label': []}
    
    # Copy image files and rename them
    for image_file in src_image_files:
        new_image_file = image_file.replace("_out", "")
        shutil.copy(os.path.join(src_image_dir, image_file), os.path.join(target_dir, new_image_file))
        copied_files['image'].append(new_image_file)
    
    # Copy label files
    for label_file in src_label_files:
        shutil.copy(os.path.join(src_label_dir, label_file), os.path.join(target_dir, label_file))
        copied_files['label'].append(label_file)
    
    # Remove mismatched files
    for image_file in copied_files['image']:
        corresponding_txt = image_file.replace('.jpg', '.txt')
        if corresponding_txt not in copied_files['label']:
            os.remove(os.path.join(target_dir, image_file))
    
    for label_file in copied_files['label']:
        corresponding_jpg = label_file.replace('.txt', '.jpg')
        if corresponding_jpg not in copied_files['image']:
            os.remove(os.path.join(target_dir, label_file))
    
    print("Copying and curation completed.")

# Define source and target directories
src_image_dir = '/media/ngoc/a normal usb/ngoc/new-val/labelimage3/transfer-done-val5/images'
src_label_dir = '/media/ngoc/a normal usb/ngoc/new-val/val5-standard/labels'
target_dir = '/media/ngoc/a normal usb/ngoc/new-val/labelimage3/lbl-img-style-transfer'

# Execute the function
copy_and_curate_files(src_image_dir, src_label_dir, target_dir)

