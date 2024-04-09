import os

# Paths to the video and image directories
video_dir = '/media/ngoc/a normal usb/ngoc-data-thesis/videos/val'
image_dir = '/media/ngoc/a normal usb/ngoc/new-val/valid-second-phase-with-val5-style-transfer-repair1/images'

# Counter for the number of matched videos
matched_videos_count = 0

# Set to hold names of matched videos
matched_videos = set()

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
        matched_videos_count += 1
        matched_videos.add(mp4_filename)

# Print the number of matched videos
print(f'Number of videos being used in those images: {matched_videos_count}')
