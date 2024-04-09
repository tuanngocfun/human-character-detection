import os
import re
from moviepy.editor import VideoFileClip

# Function to get filenames from a specific directory
def get_video_filenames(directory):
    filenames = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):
                filenames.append(file)
    return filenames

# Function to get duration of a video
def get_video_duration(video_path):
    with VideoFileClip(video_path) as clip:
        return clip.duration

if __name__ == "__main__":
    # Initialize variables
    preprocess_dir = "/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/cartoon"
    train_dir = "/media/ngoc/mydisk/ngoc/thesis/dataset/videos/train/cartoon"
    total_duration = 0.0
    
    # Get video filenames from the preprocessing and train directories
    preprocess_files = get_video_filenames(preprocess_dir)
    train_files = get_video_filenames(train_dir)
    
    # Find the matching filenames
    matching_files = set(preprocess_files).intersection(set(train_files))
    
    # Measure the duration of matching videos and sum it up
    for matching_file in matching_files:
        video_path = os.path.join(train_dir, matching_file)
        duration = get_video_duration(video_path)
        total_duration += duration
    
    # Log the total duration
    total_duration_mins = total_duration / 60.0
    print(f"Cartoon set lasts: {total_duration_mins:.2f} minutes")
