from concurrent.futures import ProcessPoolExecutor
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
import os
import shutil
import numpy as np
import logging

source_dir = '../../style-transfer/test1/origin-of-filter-frame9-&-10'
target_dir = '../../style-transfer/test1/origin-of-filter-frame9-&-10-similarity-groups'
threshold = 0.90
image_size = (100, 100)
max_workers = 24

logging.basicConfig(level=logging.INFO)

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

def image_to_vector(image_path):
    try:
        with Image.open(image_path).convert('RGB') as image:
            image = image.resize(image_size)
            return np.array(image).flatten()
    except Exception as e:
        logging.error(f"Failed to process {image_path}: {str(e)}")
        return None

def process_images(image_paths):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        vectors = list(executor.map(image_to_vector, image_paths))
    return [v for v in vectors if v is not None]

image_paths = [os.path.join(source_dir, filename) for filename in os.listdir(source_dir) if filename.endswith(".jpg")]
image_vectors = process_images(image_paths)

similarities = cosine_similarity(image_vectors)
processed_images = np.zeros(len(image_paths), dtype=bool)

# Find similar images and move them
for i, similar_indices in enumerate((similarities >= threshold) & ~processed_images):
    group = np.where(similar_indices)[0]
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

logging.info("Similarity filtering and grouping is complete.")