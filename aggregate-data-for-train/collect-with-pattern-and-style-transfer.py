import os
import shutil

# Data sources and their corresponding label paths
data_paths = {
    'data1':('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-1',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict40/labels'),
    'data2':('/home/aivn12gb/yolov8_domain_adaption_evn/test-data/complete-first-w-human-real-world-iou-95-70-conf-animation-conf90-iou95/images',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict41/labels'),
    'data3':('/home/aivn12gb/yolov8_domain_adaption_evn/style-transfer/origin-of-filter-frame9-&-10',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict44/labels'),
    'data4':('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-2',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict45/labels'),
    'data5':('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict46/labels'),
    'data6':('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-3',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict47/labels'),
    'data7':('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train1',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict50/labels'),
    'data8':('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-4',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict52/labels'),
    'data9':('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train2',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict54/labels'),
    # 'data10':('/home/aivn12gb/yolov8_domain_adaption_evn/test-data/complete-first-w-human-real-world-iou-95-70-conf-animation-conf90-iou95/similarity-images',
    #   '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict42/labels')
    'data10': ('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-5',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict56/labels'),
    'data11': ('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train3',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict57/labels'),
    'data12': ('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-6',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict61/labels'),
    'data13': ('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train4',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict62/labels'),
    'data14': ('/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-7',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict66/labels'),
    'data15': ('/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train5',
      '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict67/labels')
}

# Define the target directory for images and labels
target_images_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4/images'
target_labels_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4/labels'

# Create target directories if they do not exist
os.makedirs(target_images_dir, exist_ok=True)
os.makedirs(target_labels_dir, exist_ok=True)

def copy_files(src_dir, dest_dir, extension, label_id):
    for filename in os.listdir(src_dir):
        if filename.endswith(extension):
            src_filepath = os.path.join(src_dir, filename)
            # Append a label_id to make it unique across all data sets
            unique_filename = f"{label_id}_{filename}"
            dest_filepath = os.path.join(dest_dir, unique_filename)
            shutil.copy2(src_filepath, dest_filepath)

# Loop over all data_paths and perform the copying
for label_id, (image_dir, label_dir) in data_paths.items():
    print(f"Copying files from {image_dir} and {label_dir}...")
    
    # Copy .jpg images
    copy_files(image_dir, target_images_dir, '.jpg', label_id)
    
    # Copy .txt labels
    copy_files(label_dir, target_labels_dir, '.txt', label_id)

print("Task completed. Files have been copied.")
