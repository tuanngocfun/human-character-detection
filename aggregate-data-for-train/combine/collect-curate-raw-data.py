import os
import shutil

# Function to copy only files that have corresponding label/image files
def copy_corresponding_files(src_image_dir, src_label_dir, dest_image_dir, dest_label_dir, label_id):
    src_image_files = set(os.listdir(src_image_dir))
    src_label_files = set(os.listdir(src_label_dir))

    src_image_names = {os.path.splitext(f)[0] for f in src_image_files if f.endswith('.jpg')}
    src_label_names = {os.path.splitext(f)[0] for f in src_label_files if f.endswith('.txt')}
    
    # Find intersection set of image and label files
    common_names = src_image_names.intersection(src_label_names)
    
    for name in common_names:
        src_image_path = os.path.join(src_image_dir, f"{name}.jpg")
        src_label_path = os.path.join(src_label_dir, f"{name}.txt")
        
        unique_image_filename = f"{label_id}_{name}.jpg"
        unique_label_filename = f"{label_id}_{name}.txt"
        
        dest_image_path = os.path.join(dest_image_dir, unique_image_filename)
        dest_label_path = os.path.join(dest_label_dir, unique_label_filename)
        
        shutil.copy2(src_image_path, dest_image_path)
        shutil.copy2(src_label_path, dest_label_path)

data_paths = {
    'data1':('/home/aivn12gb/yolov8_domain_adaption_evn/dataset',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict73/labels'),
    'data2':('/home/aivn12gb/yolov8_domain_adaption_evn/filter-frame-backup',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict74/labels'),
    'data3':('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-1',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict40/labels'),
    'data4':('/home/aivn12gb/yolov8_domain_adaption_evn/filter-frame9',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict76/labels'),
    'data5':('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-2',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict45/labels'),
    'data6':('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train-raw',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict77/labels'),
    'data7':('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-3',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict47/labels'),
    'data8':('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train1',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict50/labels'),
    'data9':('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-4-raw',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict78/labels'),
    'data10': ('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train-raw2',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict79/labels'),
    'data11': ('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-5-raw',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict80/labels'),
    'data12': ('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train-raw3',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict84/labels'),
    'data13': ('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-6-raw',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict82/labels'),
    'data14': ('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train-raw4',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict83/labels'),
    'data15': ('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-7-raw',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict85/labels'),
    'data16': ('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train-raw5',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict86/labels'),
}
# 1256+658+710+355+280++331+1222+229+1598+272+736+1775+674+162+563+124

target_images_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-raw/images'
target_labels_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-raw/labels'

# Create target directories if they don't exist
os.makedirs(target_images_dir, exist_ok=True)
os.makedirs(target_labels_dir, exist_ok=True)

# Loop through each source directory and copy the files
for label_id, (image_dir, label_dir) in data_paths.items():
    print(f"Copying files from {image_dir} and {label_dir}...")
    copy_corresponding_files(image_dir, label_dir, target_images_dir, target_labels_dir, label_id)

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
