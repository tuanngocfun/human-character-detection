from concurrent.futures import ProcessPoolExecutor
from PIL import Image
import os
import shutil
import cupy as cp  # Import CuPy
import logging

source_dir = '../../test-data/merge-filter-frame-for-train'
target_dir = '../../test-data/merge-filter-frame-for-train-similarity-groups'
threshold = 0.90
image_size = (112, 112) # 5600 gpu mem
max_workers = 24
batch_size = 500

logging.basicConfig(level=logging.INFO)

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

def image_to_vector(image_path):
    try:
        with Image.open(image_path).convert('RGB') as image:
            image = image.resize(image_size)
            return cp.array(image, dtype=cp.float32).ravel()  # Use CuPy here
    except Exception as e:
        logging.error(f"Failed to process {image_path}: {str(e)}")
        return None

def process_images(image_paths):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        vectors = list(executor.map(image_to_vector, image_paths))
    return cp.array([v for v in vectors if v is not None])  # Use CuPy here

def compute_similarity_in_batches(vectors):
    total = len(vectors)
    final_matrix = cp.zeros((total, total), dtype=cp.float32)  # Use CuPy here

    for i in range(0, total, batch_size):
        start = i
        end = min(i + batch_size, total)
        batch = vectors[start:end]

        similarities = cp.dot(batch, vectors.T)  # Use CuPy here for dot product
        similarities /= cp.linalg.norm(batch, axis=1)[:, cp.newaxis]
        similarities /= cp.linalg.norm(vectors, axis=1)
        
        # Update the final similarity matrix
        final_matrix[start:end, :] = similarities
    
    return final_matrix

image_paths = [os.path.join(source_dir, filename) for filename in os.listdir(source_dir) if filename.endswith(".jpg")]
image_vectors = process_images(image_paths)
similarities = compute_similarity_in_batches(image_vectors)

processed_images = cp.zeros(len(image_paths), dtype=bool)  # Use CuPy here

# Find similar images and move them
for i, similar_indices in enumerate((similarities >= threshold)):
    group = cp.where(similar_indices)[0]  # Use CuPy here

    if len(group) == 1:
        continue

    processed_images[group] = True

    for j in group[1:]:
        source_path = image_paths[int(j)]  # Cast to int as CuPy returns them as different types
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