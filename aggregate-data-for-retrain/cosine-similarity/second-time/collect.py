import os
import shutil

def copy_files(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(('.jpg', '.txt')):
                source_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, src_dir)
                dest_file_path = os.path.join(dest_dir, relative_path, file)
                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                shutil.copy2(source_file_path, dest_file_path)

def main():
    base_dir = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction/merge-anime-split'
    sub_dirs = [
        os.path.join(base_dir, 'subdir1', 'dir1'),
        os.path.join(base_dir, 'subdir1', 'dir2'),
        os.path.join(base_dir, 'subdir1_2')
    ]
    
    target_dir = os.path.join(base_dir, 'collect')
    
    for sub_dir in sub_dirs:
        image_src_dir = os.path.join(sub_dir, 'images')
        label_src_dir = os.path.join(sub_dir, 'labels')
        
        image_dest_dir = os.path.join(target_dir, 'images')
        label_dest_dir = os.path.join(target_dir, 'labels')
        
        copy_files(image_src_dir, image_dest_dir)
        copy_files(label_src_dir, label_dest_dir)

if __name__ == "__main__":
    main()
