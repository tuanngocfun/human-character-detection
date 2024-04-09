from concurrent.futures import ProcessPoolExecutor
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from PIL import Image
import os
import shutil
import numpy as np
import logging
import time

source_dir = '../../merge-filter-frame-for-train'
target_dir = '../../merge-filter-frame-for-train-similarity-groups'
threshold = 0.90
max_workers = 24

logging.basicConfig(level=logging.INFO)

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

def image_to_vector(image_path, image_size):
    try:
        with Image.open(image_path).convert('RGB') as image:
            image = image.resize(image_size)
            return np.array(image).flatten()
    except Exception as e:
        logging.error(f"Failed to process {image_path}: {str(e)}")
        return None

def process_images(image_paths, image_size, n_components=50):
    vectors = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        vectors = list(executor.map(lambda path: image_to_vector(path, image_size), image_paths))
    vectors = [v for v in vectors if v is not None]
    
    # Apply PCA for dimensionality reduction
    pca = PCA(n_components=n_components)
    reduced_vectors = pca.fit_transform(vectors)
    return reduced_vectors

def benchmark(image_size):
    start_time = time.time()
    image_paths = [os.path.join(source_dir, filename) for filename in os.listdir(source_dir) if filename.endswith(".jpg")]
    image_vectors = process_images(image_paths, image_size)
    similarities = cosine_similarity(image_vectors)
    processed_images = np.zeros(len(image_paths), dtype=bool)
    for i, similar_indices in enumerate((similarities >= threshold) & ~processed_images):
        group = np.where(similar_indices)[0]
        if len(group) == 1:
            continue
        processed_images[group] = True
    elapsed_time = time.time() - start_time
    logging.info(f"Elapsed time for image size {image_size}: {elapsed_time} seconds")

# Run benchmark for different image sizes
for img_size in [(100, 100), (224, 224), (448, 448)]:
    benchmark(image_size=img_size)

logging.info("Similarity filtering and grouping is complete.")