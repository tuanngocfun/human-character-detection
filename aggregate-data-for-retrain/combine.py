import os
import shutil

def copy_files(src_dir, dest_dir, file_extension):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for filename in os.listdir(src_dir):
        if filename.endswith(file_extension):
            src_filepath = os.path.join(src_dir, filename)
            dest_filepath = os.path.join(dest_dir, filename)

            shutil.copy(src_filepath, dest_filepath)

def check_matching_files(img_dir, lbl_dir):
    img_files = {f.split('.')[0] for f in os.listdir(img_dir) if f.endswith('.jpg')}
    lbl_files = {f.split('.')[0] for f in os.listdir(lbl_dir) if f.endswith('.txt')}

    for img_file in img_files:
        if img_file not in lbl_files:
            print(f"Image {img_file}.jpg does not have a matching label.")

    for lbl_file in lbl_files:
        if lbl_file not in img_files:
            print(f"Label {lbl_file}.txt does not have a matching image.")

if __name__ == '__main__':
    src_img_dirs = [
        '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-retrain-subset/images',
        '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-retrain/images'
    ]
    
    src_lbl_dirs = [
        '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-retrain-subset/labels',
        '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-retrain/labels'
    ]

    dest_img_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-combine/images'
    dest_lbl_dir = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-combine/labels'

    # Copying image files
    for src_img_dir in src_img_dirs:
        copy_files(src_img_dir, dest_img_dir, '.jpg')
    
    # Copying label files
    for src_lbl_dir in src_lbl_dirs:
        copy_files(src_lbl_dir, dest_lbl_dir, '.txt')

    # Check for matching files
    check_matching_files(dest_img_dir, dest_lbl_dir)
