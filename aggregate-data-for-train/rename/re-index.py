import os

# Define the directories
train_data_dir = "/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/add-filter-fram7-to-upscale-low-pixel-train"
images_dir = os.path.join(train_data_dir, "images")
labels_dir = os.path.join(train_data_dir, "labels")

# Initialize counter for 5-digit numbering
counter = 0

# Iterate over each image file in the images directory
for image_file in os.listdir(images_dir):
    if image_file.endswith(".jpg"):
        
        # Create the new 5-digit number filename
        new_file_name = f"{counter:06d}"
        
        # Rename the image file
        os.rename(os.path.join(images_dir, image_file), os.path.join(images_dir, f"{new_file_name}.jpg"))
        
        # Rename the corresponding label file
        label_file = image_file.replace(".jpg", ".txt")
        os.rename(os.path.join(labels_dir, label_file), os.path.join(labels_dir, f"{new_file_name}.txt"))
        
        # Increment the counter
        counter += 1
