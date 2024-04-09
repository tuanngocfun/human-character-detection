import os
import shutil
from pathlib import Path

def copy_images(src_dir, dest_dir, sub_dir_pattern, start, end):
    for i in range(start, end+1):
        sub_dir_name = sub_dir_pattern.format(i)
        sub_dir_path = os.path.join(src_dir, sub_dir_name)
        
        if os.path.exists(sub_dir_path):
            for img_file in os.listdir(sub_dir_path):
                if img_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    src_file_path = os.path.join(sub_dir_path, img_file)
                    dest_file_path = os.path.join(dest_dir, f"{sub_dir_name}_{img_file}")
                    shutil.copy2(src_file_path, dest_file_path)
        else:
            print(f"Subdirectory {sub_dir_name} does not exist in {src_dir}")

def main():
    # Define the source and destination directories
    src_dir_cartoon = "/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon"
    src_dir_anime = "/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-anime"
    dest_dir = "/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/merge-anime-cartoon-similarity-groups"

    # Create the destination directory if it doesn't exist
    Path(dest_dir).mkdir(parents=True, exist_ok=True)
    
    # Copy images from cartoon subdirectories
    copy_images(src_dir_cartoon, dest_dir, "merge-filter-cartoon-frame-for-train{}", 1, 3)
    
    # Copy images from anime subdirectories
    copy_images(src_dir_anime, dest_dir, "merge-filter-anime-frame-for-train{}", 1, 7)

if __name__ == "__main__":
    main()
