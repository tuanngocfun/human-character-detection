import cv2
import os

def get_video_fps(video_path):
    video = cv2.VideoCapture(video_path)
    # Get the frames per second of the video
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    return fps

def average_fps(directory, all_fps_list):
    local_fps_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                video_path = os.path.join(root, file)
                fps = get_video_fps(video_path)
                local_fps_list.append(fps)
                all_fps_list.append(fps)  # Add to the overall list
                print(f'Video {file} has {fps} FPS.')
    if local_fps_list:
        return sum(local_fps_list) / len(local_fps_list)
    else:
        return 0

# Set directories
anime_directory = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/anime'
cartoon_directory = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/cartoon'

# List to hold all FPS values
all_fps = []

# Calculate average FPS for each set
anime_avg_fps = average_fps(anime_directory, all_fps)
cartoon_avg_fps = average_fps(cartoon_directory, all_fps)

print(f'The average FPS for anime videos is: {anime_avg_fps}')
print(f'The average FPS for cartoon videos is: {cartoon_avg_fps}')

# Calculate the overall average FPS for the entire train set
overall_avg_fps = sum(all_fps) / len(all_fps) if all_fps else 0
print(f'The overall average FPS for the train set (anime and cartoon) is: {overall_avg_fps}')
