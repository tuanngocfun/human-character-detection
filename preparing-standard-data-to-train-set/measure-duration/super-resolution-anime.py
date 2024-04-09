import os
import subprocess
import logging

logging.basicConfig(filename="anime_video_duration.log", level=logging.INFO)

# Paths
video_path = "/media/ngoc/mydisk/ngoc/thesis/dataset/videos/train/anime"
image_path = "/media/ngoc/a normal usb/ngoc/training-set/super-resolution-images/kaggle/working/Real-ESRGAN/result/anime"

# List all files in the directories
video_files = [f for f in os.listdir(video_path) if f.endswith('.mp4')]
image_files = [f for f in os.listdir(image_path) if f.endswith('.png')]

# Initialize total duration
total_duration = 0

# Loop through each video file to see if it matches any image file
for video_file in video_files:
    video_name = os.path.splitext(video_file)[0]  # Extract the name without extension
    corresponding_image_file = f"{video_name}.png"

    # If there is a match
    if corresponding_image_file in image_files:
        full_video_path = os.path.join(video_path, video_file)

        # Use ffprobe to get the video duration in seconds
        cmd = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {full_video_path}"
        duration_str = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
        duration = float(duration_str)

        # Add to the total duration
        total_duration += duration

# Log the total duration in minutes
total_duration_mins = total_duration / 60.0
logging.info(f"anime set last: {total_duration_mins:.2f} mins")
