import os

# Define the paths to the images and labels directories
images_dir = "/media/ngoc/a normal usb/ngoc/test-set2/refine/images"
labels_dir = "/media/ngoc/a normal usb/ngoc/test-set2/refine/labels"

def main():
    # First pass: Check images against labels
    image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
    
    for image_file in image_files:
        base_name = os.path.splitext(image_file)[0]
        label_file = os.path.join(labels_dir, f"{base_name}.txt")
        
        if not os.path.exists(label_file):
            image_file_path = os.path.join(images_dir, image_file)
            os.remove(image_file_path)
            print(f"Removed {image_file_path} as no corresponding label file was found.")
    
    # Second pass: Check labels against images
    label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]
    
    for label_file in label_files:
        base_name = os.path.splitext(label_file)[0]
        image_file = os.path.join(images_dir, f"{base_name}.jpg")
        
        if not os.path.exists(image_file):
            label_file_path = os.path.join(labels_dir, label_file)
            os.remove(label_file_path)
            print(f"Removed {label_file_path} as no corresponding image file was found.")

if __name__ == "__main__":
    main()

