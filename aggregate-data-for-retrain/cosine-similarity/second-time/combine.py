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
    base_dir = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction'
    prev_collect_dir = os.path.join(base_dir, 'merge-anime-split', 'collect')
    merge_cartoon_dir = os.path.join(base_dir, 'merge-cartoon')
    
    target_dir = os.path.join(base_dir, 'second-time')
    
    src_dirs = [
        (os.path.join(prev_collect_dir, 'images'), os.path.join(target_dir, 'images')),
        (os.path.join(prev_collect_dir, 'labels'), os.path.join(target_dir, 'labels')),
        (os.path.join(merge_cartoon_dir, 'images'), os.path.join(target_dir, 'images')),
        (os.path.join(merge_cartoon_dir, 'labels'), os.path.join(target_dir, 'labels'))
    ]
    
    for src_dir, dest_dir in src_dirs:
        copy_files(src_dir, dest_dir)

if __name__ == "__main__":
    main()
