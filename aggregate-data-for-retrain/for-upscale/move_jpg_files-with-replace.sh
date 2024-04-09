#!/bin/bash

SOURCE_DIR="/home/aivn12s2/data/upscale-dataset"
TARGET_DIR="/home/aivn12s2/data/upscale-dataset/aggregate-upscale-data"

mkdir -p "$TARGET_DIR"

find "$SOURCE_DIR/anime/" -type f -name "*.jpg" -exec mv {} "$TARGET_DIR" \;

find "$SOURCE_DIR/cartoon/" -type f -name "*.jpg" -exec mv {} "$TARGET_DIR" \;

find "$SOURCE_DIR/merge-similarity-groups-anime-cartoon/" -type f -name "*.jpg" -exec mv {} "$TARGET_DIR" \;

echo "All .jpg files have been moved to $TARGET_DIR"

