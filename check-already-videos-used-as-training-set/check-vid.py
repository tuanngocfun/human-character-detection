import os
import logging
from termcolor import colored

# Initialize logging
logging.basicConfig(level=logging.INFO)

def get_video_names(directory):
    video_names = set()
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".mp4"):
                video_name = os.path.splitext(filename)[0]
                video_names.add(video_name)
    except FileNotFoundError:
        logging.error(f"Directory {directory} not found.")
    return video_names

# Define the paths
directory_path1 = 'vid'
directory_path2 = 'videos/train/cartoon'

# Get the video names from each directory
videos_in_dir1 = get_video_names(directory_path1)
videos_in_dir2 = get_video_names(directory_path2)

# Find the duplicated video names between two directories
duplicated_videos = videos_in_dir1.intersection(videos_in_dir2)

# Beautify log output
separator = colored("==================================================", "yellow")
path1_colored = colored(os.path.abspath(directory_path1), "blue")
path2_colored = colored(os.path.abspath(directory_path2), "green")

# Log output
logging.info(separator)
logging.info(f"Number of duplicated video names: {colored(len(duplicated_videos), 'magenta')}")
logging.info(separator)
logging.info(f"Between the directories:")
logging.info(f"1st Path: {path1_colored}")
logging.info(f"2nd Path: {path2_colored}")
logging.info(separator)

# List all duplicated video names
if duplicated_videos:
    logging.info(colored(f"List of duplicated video names:", "yellow"))
    for video_name in duplicated_videos:
        logging.info(colored(video_name, "cyan"))
else:
    logging.info(colored(f"No duplicated video names found.", "red"))
logging.info(separator)
