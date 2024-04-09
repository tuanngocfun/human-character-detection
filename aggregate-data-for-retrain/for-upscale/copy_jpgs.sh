#!/bin/bash

SOURCE_DIR="/home/aivn12s2/Downloads/upscale"
TARGET_DIR="/home/aivn12s2/Downloads/upscale-for-all-in-one"

mkdir -p "$TARGET_DIR"

find "$SOURCE_DIR" -name '*.jpg' -exec cp {} "$TARGET_DIR" \;

echo "All .jpg files have been copied to $TARGET_DIR."

