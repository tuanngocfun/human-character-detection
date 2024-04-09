import os

def remove_noncorresponding_files(target_images_dir, target_labels_dir):
    # List all the image and label files
    image_files = set(os.listdir(target_images_dir))
    label_files = set(os.listdir(target_labels_dir))
    
    # Create sets containing just the filenames without extensions for easy comparison
    image_names = {os.path.splitext(f)[0] for f in image_files if f.endswith('.jpg')}
    label_names = {os.path.splitext(f)[0] for f in label_files if f.endswith('.txt')}
    
    # Find .jpg files that do not have corresponding .txt files and remove them
    for image_name in image_names - label_names:
        image_path = os.path.join(target_images_dir, f"{image_name}.jpg")
        os.remove(image_path)
        print(f"Removed {image_path}")
        
    # Find .txt files that do not have corresponding .jpg files and remove them
    for label_name in label_names - image_names:
        label_path = os.path.join(target_labels_dir, f"{label_name}.txt")
        os.remove(label_path)
        print(f"Removed {label_path}")

# Directories for image and label files
target_images_dir = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/add-filter-fram7-to-upscale-low-pixel-train/images'
target_labels_dir = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/add-filter-fram7-to-upscale-low-pixel-train/labels'

# Call the function to remove non-corresponding files
remove_noncorresponding_files(target_images_dir, target_labels_dir)
