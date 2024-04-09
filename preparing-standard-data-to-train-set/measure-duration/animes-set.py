from moviepy.editor import VideoFileClip
import os

# Define the path to the video files
video_directory_path = '/media/ngoc/mydisk/ngoc/thesis/dataset/videos/train/anime'

# Initialize the total duration variable
total_duration = 0.0

# Loop through each video file in the directory
for filename in os.listdir(video_directory_path):
    if filename.endswith('.mp4'):
        filepath = os.path.join(video_directory_path, filename)
        
        # Use moviepy to open the video file and get its duration
        with VideoFileClip(filepath) as clip:
            duration = clip.duration
            total_duration += duration  # Add to the total duration

# Calculate total duration in minutes
total_duration_minutes = total_duration / 60.0

# Log the result
print(f"Anime set lasts: {total_duration_minutes:.2f} minutes")
