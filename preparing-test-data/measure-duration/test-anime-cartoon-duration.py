import os
from moviepy.editor import VideoFileClip

# Paths to the video directories
anime_dir = '/media/ngoc/a normal usb/ngoc-data-thesis/videos/test'
cartoon_dir = '/media/ngoc/a normal usb/ngoc-data-thesis/videos/test2'

# Lists to hold durations of matched videos for each genre
anime_durations = []
cartoon_durations = []

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

# Get all mp4 files from the specified directories
anime_mp4_files = list(find_mp4_files(anime_dir))
cartoon_mp4_files = list(find_mp4_files(cartoon_dir))

# Iterate through all mp4 files to calculate video duration
for mp4_file in anime_mp4_files:
    with VideoFileClip(mp4_file) as video:
        anime_durations.append(video.duration)

for mp4_file in cartoon_mp4_files:
    with VideoFileClip(mp4_file) as video:
        cartoon_durations.append(video.duration)

# Calculate the total duration in minutes for each genre
total_anime_duration_minutes = sum(anime_durations) / 60
total_cartoon_duration_minutes = sum(cartoon_durations) / 60

print(f'Anime validation set: {total_anime_duration_minutes:.2f} minutes')
print(f'Cartoon validation set: {total_cartoon_duration_minutes:.2f} minutes')
