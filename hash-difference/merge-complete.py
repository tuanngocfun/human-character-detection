import os
import shutil

# Define the source directories
source_dirs = {
    'images': [
        '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/train-dataset-raw-images/images',
        '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/dataset-of-hash-difference-first-time-merge-similarity/images'
    ],
    'labels': [
        '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/train-dataset-raw-images/labels',
        '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/dataset-of-hash-difference-first-time-merge-similarity/labels'
    ]
}

# Define the target directories
target_dir_base = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/hash-difference-first-time'
target_dirs = {
    'images': os.path.join(target_dir_base, 'images'),
    'labels': os.path.join(target_dir_base, 'labels')
}

# Function to create directories if they don't exist
def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to copy files
def copy_files(file_type, extension):
    for source_dir in source_dirs[file_type]:
        for filename in os.listdir(source_dir):
            if filename.endswith(extension):
                shutil.copy(os.path.join(source_dir, filename), target_dirs[file_type])

# Create target directories
create_dir_if_not_exists(target_dirs['images'])
create_dir_if_not_exists(target_dirs['labels'])

# Copy .jpg and .txt files
copy_files('images', '.jpg')
copy_files('labels', '.txt')

print("Files copied successfully.")

