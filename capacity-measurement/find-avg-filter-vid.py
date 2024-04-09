import os
from pathlib import Path

# Define the path to the directory containing filter-vid{number} subdirectories
base_path = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/cartoon'

# List all the subdirectories in the base path that match the filter-vid pattern
subdirs = [d for d in os.listdir(base_path) if d.startswith('filter-vid') and os.path.isdir(os.path.join(base_path, d))]

# Calculate the size of each filter-vid{number} directory
dir_sizes = {}
for subdir in subdirs:
    subdir_path = Path(base_path) / subdir
    total_size_mb = sum(f.stat().st_size for f in subdir_path.glob('**/*.mp4')) / (1024 * 1024)
    dir_sizes[subdir] = total_size_mb

# Calculate the average directory size
average_size_mb = sum(dir_sizes.values()) / len(dir_sizes)

# Find the directory with the size closest to the average
closest = min(dir_sizes, key=lambda x: abs(dir_sizes[x] - average_size_mb))

# Output the result
print(f"The directory closest to the average size is: {closest}")
print(f"Size: {dir_sizes[closest]:.2f} MB (Average size: {average_size_mb:.2f} MB)")
