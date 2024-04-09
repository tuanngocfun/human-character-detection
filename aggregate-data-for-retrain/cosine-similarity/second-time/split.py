import os
import shutil

def split_images(src_dir, dest_dir1, dest_dir2, split_count):
    os.makedirs(dest_dir1, exist_ok=True)
    os.makedirs(dest_dir2, exist_ok=True)

    # Get a list of all the images in the source directory
    images = [f for f in os.listdir(src_dir) if f.endswith('.jpg')]
    
    # Ensure there are enough images to split
    total_images = len(images)
    if total_images < split_count * 2:
        raise ValueError(f'There are only {total_images} images, but {split_count * 2} are required.')

    # Split the images into two groups
    for i, image in enumerate(images):
        # Determine the destination directory for this image
        dest_dir = dest_dir1 if i < split_count else dest_dir2
        # Move the image to the destination directory
        shutil.move(os.path.join(src_dir, image), os.path.join(dest_dir, image))

src_dir = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction/merge-anime-split/subdir1/sub_dir_1_1'
dest_dir1 = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction/merge-anime-split/subdir1/sub1'
dest_dir2 = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction/merge-anime-split/subdir1/sub2'

split_count = 15000
split_images(src_dir, dest_dir1, dest_dir2, split_count)
