import os
import imagehash
from PIL import Image

def find_duplicates(directory):
    hashes = {}
    duplicate_count = 0

    # Process each image in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                # Compute the perceptual hash of the image
                img_hash = imagehash.phash(img)
                if img_hash in hashes:
                    duplicate_count += 1
                else:
                    hashes[img_hash] = filename

    total_images = len(hashes) + duplicate_count
    duplication_rate = duplicate_count / total_images if total_images > 0 else 0

    return duplication_rate

directory_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/train-cs-and-hd-prep/images'
duplication_rate = find_duplicates(directory_path)

# Writing results to a .txt file
parent_directory = os.path.basename(os.path.dirname(directory_path))
result_file_name = f"{parent_directory}.txt"
with open(result_file_name, 'w') as file:
    file.write(f"Rate of Image Duplication: {duplication_rate:.2%}\n")

print(f"Rate of Image Duplication: {duplication_rate:.2%}")
print(f"Results written to {result_file_name}")

