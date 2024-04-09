import os
import shutil

def combine_images(source_dirs, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for source_dir in source_dirs:
        for filename in os.listdir(source_dir):
            if filename.endswith(".jpg"):
                source_filepath = os.path.join(source_dir, filename)
                target_filepath = os.path.join(target_dir, filename)
                
                counter = 0
                while os.path.exists(target_filepath):
                    counter += 1
                    target_filepath = os.path.join(target_dir, f"{filename.split('.')[0]}_{counter}.jpg")
                
                shutil.copy2(source_filepath, target_filepath)
                print(f"Image {filename} from {source_dir} has been moved to {target_filepath}")

source_dirs = [
    '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/extract-cartoon-update',
    '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/extract-anime-update',
    '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/merge-anime-cartoon-similarity-groups'
]

target_dir = "/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/train-set"

combine_images(source_dirs, target_dir)
