import os
import shutil
import re

# Define the paths for the source and target directories
anime_source_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/anime'
cartoon_source_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/cartoon'
merge_target_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/merge-for-train-set'
anime_target_subdir = 'merge-anime-videos'
cartoon_target_subdir = 'merge-cartoon-videos'

# Function to copy the contents of directories matching 'filter-vid{numbers}'
def copy_filtered_videos(source_dir, target_subdir):
    # Create the target directory if it doesn't exist
    target_dir = os.path.join(merge_target_dir, target_subdir)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Identify and copy the directories that match the 'filter-vid{numbers}' pattern
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path) and re.match(r'filter-vid\d+', item):
            for filename in os.listdir(item_path):
                # We're only interested in .mp4 files within these directories
                if filename.endswith('.mp4'):
                    source_file = os.path.join(item_path, filename)
                    target_file = os.path.join(target_dir, filename)
                    shutil.copy2(source_file, target_file)
                    print(f"Copied {filename} from {item} to {target_subdir}")

# Copy anime video directories
copy_filtered_videos(anime_source_dir, anime_target_subdir)

# Copy cartoon video directories
copy_filtered_videos(cartoon_source_dir, cartoon_target_subdir)

print("Video files have been copied successfully.")
