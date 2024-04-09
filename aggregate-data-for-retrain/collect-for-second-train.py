import os
import shutil

source_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4/images'

subset_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-retrain/images'

dest_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-retrain-subset/images'

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

source_images = set([f for f in os.listdir(source_dir) if f.endswith('.jpg')])
subset_images = set([f for f in os.listdir(subset_dir) if f.endswith('.jpg')])

# Find the difference between the sets to get images not in subset
images_to_copy = source_images - subset_images

# Copy the images not in subset from source to destination directory
for image in images_to_copy:
    shutil.copy(os.path.join(source_dir, image), os.path.join(dest_dir, image))

print(f"Copied {len(images_to_copy)} images from {source_dir} to {dest_dir}")
