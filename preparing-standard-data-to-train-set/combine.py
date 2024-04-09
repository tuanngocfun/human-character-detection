import os
import shutil

def combine_files(src_dirs, target_dir):
    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    for src_dir in src_dirs:
        # List all files in source directory
        files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
        
        # Copy files to target directory
        for file in files:
            shutil.copy(os.path.join(src_dir, file), os.path.join(target_dir, file))

# Directories for anime files
anime_src_dirs = [
    '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/archive/combine-anime/combine-anime',
    '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-anime/re-combine-anime'
]

anime_target_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-anime-update'

# Directories for cartoon files
cartoon_src_dirs = [
    '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/archive/combine-cartoon/combine-cartoon',
    '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon/re-combine-cartoon'
]

cartoon_target_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon-update'

# Combine files
combine_files(anime_src_dirs, anime_target_dir)
combine_files(cartoon_src_dirs, cartoon_target_dir)
