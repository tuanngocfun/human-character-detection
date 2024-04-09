#!/bin/bash

# Define the source and target directories
SOURCE_DIR="/home/aivn12s2/data/upscale-dataset"
TARGET_DIR="/home/aivn12s2/data/upscale-dataset/aggregate-upscale-data"

# Create the target directory if it does not exist
mkdir -p "$TARGET_DIR"

# Move .jpg files from anime subdirectories
find "$SOURCE_DIR/anime/" -type f -name "*.jpg" -exec mv {} "$TARGET_DIR" \;

# Move .jpg files from cartoon subdirectories
find "$SOURCE_DIR/cartoon/" -type f -name "*.jpg" -exec mv {} "$TARGET_DIR" \;

# Move .jpg files from merge-similarity-groups-anime-cartoon subdirectory
find "$SOURCE_DIR/merge-similarity-groups-anime-cartoon/" -type f -name "*.jpg" -exec mv {} "$TARGET_DIR" \;

# Print completion message
echo "All .jpg files have been moved to $TARGET_DIR"

