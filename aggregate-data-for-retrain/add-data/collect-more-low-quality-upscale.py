import os
import shutil

# Function to copy only files that have corresponding label/image files
def copy_corresponding_files(src_image_dir, src_label_dir, dest_image_dir, dest_label_dir):
    src_image_files = set(os.listdir(src_image_dir))
    src_label_files = set(os.listdir(src_label_dir))

    src_image_names = {os.path.splitext(f)[0] for f in src_image_files if f.endswith('.jpg')}
    src_label_names = {os.path.splitext(f)[0] for f in src_label_files if f.endswith('.txt')}
    
    # Find intersection set of image and label files
    common_names = src_image_names.intersection(src_label_names)
    
    for name in common_names:
        src_image_path = os.path.join(src_image_dir, f"{name}.jpg")
        src_label_path = os.path.join(src_label_dir, f"{name}.txt")
        
        dest_image_path = os.path.join(dest_image_dir, f"{name}.jpg")
        dest_label_path = os.path.join(dest_label_dir, f"{name}.txt")
        
        shutil.copy2(src_image_path, dest_image_path)
        shutil.copy2(src_label_path, dest_label_path)

data_paths = {
    'data1': ('/media/ngoc/a normal usb/ngoc/training-set/aggregate4-upscale-low-quality-with-manually-lbl/images',
              '/media/ngoc/a normal usb/ngoc/training-set/aggregate4-upscale-low-quality-with-manually-lbl/labels'),
    'data2': ('/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/add-filter-fram7-to-upscale-low-pixel-train/images',
              '/media/ngoc/a normal usb/ngoc/thesis/ultralytics/runs/detect/predict32/labels'),
}

target_images_dir = '/media/ngoc/a normal usb/ngoc/training-set/aggregate4-upscale-low-quality-with-manually-lbl-adding-data/images'
target_labels_dir = '/media/ngoc/a normal usb/ngoc/training-set/aggregate4-upscale-low-quality-with-manually-lbl-adding-data/labels'

# Create target directories if they don't exist
os.makedirs(target_images_dir, exist_ok=True)
os.makedirs(target_labels_dir, exist_ok=True)

# Loop through each source directory and copy the files
for _, (image_dir, label_dir) in data_paths.items():
    print(f"Copying files from {image_dir} and {label_dir}...")
    copy_corresponding_files(image_dir, label_dir, target_images_dir, target_labels_dir)

# Function to remove non-corresponding files from target directories
def remove_noncorresponding_files(target_images_dir, target_labels_dir):
    image_files = set(os.listdir(target_images_dir))
    label_files = set(os.listdir(target_labels_dir))
    
    image_names = {os.path.splitext(f)[0] for f in image_files if f.endswith('.jpg')}
    label_names = {os.path.splitext(f)[0] for f in label_files if f.endswith('.txt')}
    
    for image_name in image_names - label_names:
        image_path = os.path.join(target_images_dir, f"{image_name}.jpg")
        os.remove(image_path)
        print(f"Removed {image_path}")
        
    for label_name in label_names - image_names:
        label_path = os.path.join(target_labels_dir, f"{label_name}.txt")
        os.remove(label_path)
        print(f"Removed {label_path}")

# Remove non-corresponding files from the target directories
remove_noncorresponding_files(target_images_dir, target_labels_dir)

print("Task completed. Files have been copied and non-corresponding files have been removed.")
