import os
import shutil

# Source directory
src_dir = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction/merge-anime'

# Destination directory
dest_dir = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction/merge-cartoon-split'

# Max files in each sub-directory
max_files = 30000

def move_files(src, dest, max_files):
    if not os.path.exists(dest):
        os.makedirs(dest)
        
    files = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f))]
    
    count = 0
    sub_dir_count = 1
    
    for f in files:
        if count % max_files == 0:
            sub_dir = os.path.join(dest, f'sub_dir_1_{sub_dir_count}')
            os.makedirs(sub_dir)
            sub_dir_count += 1
        
        src_file_path = os.path.join(src, f)
        dest_file_path = os.path.join(sub_dir, f)
        
        shutil.move(src_file_path, dest_file_path)
        
        count += 1

move_files(src_dir, dest_dir, max_files)