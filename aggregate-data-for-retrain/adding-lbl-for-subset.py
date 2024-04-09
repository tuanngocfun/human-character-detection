import os
import shutil

def copy_labels(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    for filename in os.listdir(src_dir):
        if filename.endswith('.txt'):
            src_path = os.path.join(src_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            shutil.copy(src_path, dest_path)

def check_corresponding_images(label_dir, image_dir):
    missing_images = []
    for filename in os.listdir(label_dir):
        if filename.endswith('.txt'):
            image_filename = filename.replace('.txt', '.jpg')
            image_path = os.path.join(image_dir, image_filename)
            
            if not os.path.exists(image_path):
                missing_images.append(image_filename)
                
    return missing_images

if __name__ == "__main__":
    label_src_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/predict89/labels'
    label_dest_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-retrain-subset/labels'
    image_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-retrain-subset/images'
    
    copy_labels(label_src_dir, label_dest_dir)
    
    missing_images = check_corresponding_images(label_dest_dir, image_dir)
    
    if missing_images:
        print(f"Missing corresponding images for the following labels: {missing_images}")
    else:
        print("All label files have corresponding image files.")
