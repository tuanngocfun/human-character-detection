import os
import shutil

def safe_copy(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"Copied {src} to {dest}")
    except Exception as e:
        print(f"Failed to copy {src} to {dest}. Error: {e}")

# Define source and target directories for labels
label_sources = [
    "/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict65/labels",
    "/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict63/labels"
]
label_target = "/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/mix-detection-training-lbl/train29-real-world-human-weight/labels"

# Create target directory for labels if it doesn't exist
os.makedirs(label_target, exist_ok=True)

# Copying all .txt files from both label sources to label target
for source in label_sources:
    if os.path.exists(source):
        for filename in os.listdir(source):
            if filename.endswith(".txt"):
                safe_copy(os.path.join(source, filename), label_target)
    else:
        print(f"Source directory {source} does not exist.")

# Define source and target directories for images
image_source = "/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate3/images"
image_target = "/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/mix-detection-training-lbl/train29-real-world-human-weight/images"

# Create target directory for images if it doesn't exist
os.makedirs(image_target, exist_ok=True)

# Copying all .jpg files from image_source to image_target
if os.path.exists(image_source):
    for filename in os.listdir(image_source):
        if filename.endswith(".jpg"):
            safe_copy(os.path.join(image_source, filename), image_target)
else:
    print(f"Image source directory {image_source} does not exist.")

print("File copying is complete.")