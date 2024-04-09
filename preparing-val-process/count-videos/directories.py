import os
from collections import defaultdict

# Paths to the video and image directories
video_dir = '/media/ngoc/a normal usb/ngoc-data-thesis/videos/val'
image_dir = '/media/ngoc/a normal usb/ngoc/new-val/valid-second-phase-with-val5-style-transfer-repair1/images'

# Dictionary to hold the count of matched videos for each directory
directory_video_count = defaultdict(int)

# Set to hold names of jpg files for matching
jpg_files = set()

# Helper function to find all jpg files under a directory
def find_jpg_files(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.jpg'):
                # Remove the 'frame_{number}.jpg' part to match with video filenames
                cleaned_name = file.split('_frame_')[0]
                jpg_files.add(cleaned_name)

# Populate the jpg_files set
find_jpg_files(image_dir)

# Helper function to recursively find all mp4 files under a directory and count matches
def find_and_count_mp4_files(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.mp4'):
                mp4_filename = file.replace('.mp4', '')
                if mp4_filename in jpg_files:
                    directory_video_count[root] += 1

# Find and count mp4 files
find_and_count_mp4_files(video_dir)

# Print the counts
for directory, count in directory_video_count.items():
    print(f"{directory}: {count} videos")
