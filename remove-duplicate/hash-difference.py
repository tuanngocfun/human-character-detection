from concurrent.futures import ProcessPoolExecutor
from PIL import Image
import os
import shutil
import logging
import numpy as np
import imagehash

# Configuration
source_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/hash-difference-second-time/images'
target_dir = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/hash-difference-second-time/images-similarity-groups'
hash_diff_threshold = 10
max_workers = 24
batch_size = 500

logging.basicConfig(level=logging.INFO)

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

def image_to_hash(image_path):
    try:
        with Image.open(image_path).convert('RGB') as image:
            return imagehash.average_hash(image)
    except Exception as e:
        logging.error(f"Failed to process {image_path}: {str(e)}")
        return None

def process_images(image_paths):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        hashes = list(executor.map(image_to_hash, image_paths))
    return hashes

def compute_hash_differences(hashes):
    total = len(hashes)
    final_matrix = np.zeros((total, total), dtype=int)

    for i, hash1 in enumerate(hashes):
        for j, hash2 in enumerate(hashes):
            if hash1 and hash2:  # Ensure both hashes are valid
                final_matrix[i][j] = hash1 - hash2

    return final_matrix

image_paths = [os.path.join(source_dir, filename) for filename in os.listdir(source_dir) if filename.endswith(".jpg")]
image_hashes = process_images(image_paths)
hash_differences = compute_hash_differences(image_hashes)
processed_images = np.zeros(len(image_paths), dtype=bool)

# Find similar images and move them
for i, similar_indices in enumerate((hash_differences <= hash_diff_threshold)):
    group = np.where(similar_indices)[0]

    if len(group) == 1:
        continue

    processed_images[group] = True

    for j in group[1:]:
        source_path = image_paths[j]
        target_path = os.path.join(target_dir, os.path.basename(source_path))
        logging.info(f"Moving from {source_path} to {target_path}")

        if os.path.exists(source_path):
            try:
                shutil.move(source_path, target_path)
            except Exception as e:
                logging.error(f"Failed to move {source_path}: {str(e)}")
        else:
            logging.error(f"Source file not found: {source_path}")

logging.info("Hash difference based grouping is complete.")
