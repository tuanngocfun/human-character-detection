from concurrent.futures import ProcessPoolExecutor
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
import os
import shutil
import numpy as np
import logging

#source_dir = '../../dataset/preprocessing-train-set/extract-cartoon/merge-filter-cartoon-frame-for-train3'
#target_dir = '../../dataset/preprocessing-train-set/extract-cartoon/merge-filter-cartoon-frame-for-train3-similarity-groups'
source_dir = '/media/ngoc/a normal usb/ngoc-data-thesis/dataset/merge-filter-cartoon-frame-for-train7-similarity-groups/kaggle/working/merge-filter-cartoon-frame-for-train7'
target_dir = '/media/ngoc/a normal usb/ngoc-data-thesis/dataset/merge-filter-cartoon-frame-for-train7-similarity-groups/kaggle/working/merge-filter-cartoon-frame-for-train7-similarity-groups'
threshold = 0.90
image_size = (224, 224)
max_workers = 24
batch_size = 500

logging.basicConfig(level=logging.INFO)

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

def image_to_vector(image_path):
    try:
        with Image.open(image_path).convert('RGB') as image:
            image = image.resize(image_size)
            return np.array(image, dtype=np.float32).flatten()
    except Exception as e:
        logging.error(f"Failed to process {image_path}: {str(e)}")
        return None

def process_images(image_paths):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        vectors = list(executor.map(image_to_vector, image_paths))
    return np.array([v for v in vectors if v is not None])

def compute_similarity_in_batches(vectors):
    total = len(vectors)
    final_matrix = np.zeros((total, total))

    for i in range(0, total, batch_size):
        start = i
        end = min(i + batch_size, total)
        batch = vectors[start:end]
        
        similarities = cosine_similarity(batch, vectors)
        
        # Update the final similarity matrix
        final_matrix[start:end, :] = similarities
    
    return final_matrix

image_paths = [os.path.join(source_dir, filename) for filename in os.listdir(source_dir) if filename.endswith(".jpg")]
image_vectors = process_images(image_paths)
similarities = compute_similarity_in_batches(image_vectors)
processed_images = np.zeros(len(image_paths), dtype=bool)

# Find similar images and move them
for i, similar_indices in enumerate((similarities >= threshold)):
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

logging.info("Similarity filtering and grouping is complete.")
