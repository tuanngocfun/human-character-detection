import os
from moviepy.editor import VideoFileClip

# Paths to the video and image directories
video_dir = '/media/ngoc/a normal usb/ngoc-data-thesis/videos/val'
image_dir = '/media/ngoc/a normal usb/ngoc/new-val/valid-second-phase-with-val5-style-transfer-repair1/images'

# List to hold durations of matched videos
durations = []

# Helper function to recursively find all mp4 files under a directory
def find_mp4_files(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.mp4'):
                yield os.path.join(root, file)

# Helper function to find all jpg files under a directory
def find_jpg_files(root_dir):
    jpg_files = set()
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.jpg'):
                # Remove the 'frame_{number}.jpg' part to match with video filenames
                cleaned_name = file.split('_frame_')[0]
                jpg_files.add(cleaned_name)
    return jpg_files

# Get all jpg and mp4 file names
jpg_files = find_jpg_files(image_dir)
mp4_files = find_mp4_files(video_dir)

# Iterate through all mp4 files to check if a matching jpg file exists
for mp4_file in mp4_files:
    mp4_filename = os.path.basename(mp4_file).replace('.mp4', '')

    if mp4_filename in jpg_files:
        # Calculate video duration
        with VideoFileClip(mp4_file) as video:
            duration = video.duration
            durations.append(duration)

# Calculate the total duration in minutes
total_duration_minutes = sum(durations) / 60
print(f'Validation set: {total_duration_minutes:.2f} minutes')
