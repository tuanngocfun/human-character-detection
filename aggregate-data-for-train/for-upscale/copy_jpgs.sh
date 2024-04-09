#!/bin/bash

# Define the source and target directories
SOURCE_DIR="/home/aivn12s2/Downloads/upscale"
TARGET_DIR="/home/aivn12s2/Downloads/upscale-for-all-in-one"

# Create the target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Find all .jpg files and copy them to the target directory
find "$SOURCE_DIR" -name '*.jpg' -exec cp {} "$TARGET_DIR" \;

echo "All .jpg files have been copied to $TARGET_DIR."

