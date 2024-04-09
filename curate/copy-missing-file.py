import os
import shutil

def copy_missing_files(src_path, dst_path):
    # List files in source and destination directories
    src_files = set(os.listdir(src_path))
    dst_files = set(os.listdir(dst_path))

    # Find missing files
    missing_files = src_files - dst_files

    # Copy missing files from source to destination
    for missing_file in missing_files:
        src_file_path = os.path.join(src_path, missing_file)
        dst_file_path = os.path.join(dst_path, missing_file)
        shutil.copy2(src_file_path, dst_file_path)
        print(f"Copied {missing_file} to {dst_file_path}")

if __name__ == '__main__':
    src_path = '/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train'
    dst_path = '/home/aivn12gb/yolov8_domain_adaption_evn/Real-ESRGAN/result/merge-filter-frame-for-train'
    
    # Check if the paths exist
    if not os.path.exists(src_path):
        print(f"Source path {src_path} does not exist!")
    elif not os.path.exists(dst_path):
        print(f"Destination path {dst_path} does not exist!")
    else:
        copy_missing_files(src_path, dst_path)
