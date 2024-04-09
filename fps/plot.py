import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

def get_video_fps(video_path):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    return fps

def plot_fps_for_videos(videos_fps, category):
    titles = [v[0] for v in videos_fps]
    fps_values = [v[1] for v in videos_fps]

    # Calculate the average FPS
    average_fps = np.mean(fps_values)
    
    # Plotting
    plt.figure(figsize=(14, 7))
    y_pos = np.arange(len(titles))
    plt.bar(y_pos, fps_values, alpha=0.7)
    
    # Add the average FPS line
    plt.axhline(y=average_fps, color='r', linestyle='-', label=f'Average FPS: {average_fps:.2f}')
    
    # Add some text for labels and title
    plt.xlabel('Video Titles')
    plt.ylabel('Frames Per Second (FPS)')
    plt.title(f'FPS of {category} Videos and Average FPS')
    
    # Add video titles to the x-axis
    plt.xticks(y_pos, titles, rotation=90)  # Rotate the titles to fit them on the x-axis
    
    plt.legend()
    plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
    plt.show()

def average_fps(directory, all_fps_list, videos_fps_list):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                video_path = os.path.join(root, file)
                fps = get_video_fps(video_path)
                all_fps_list.append(fps)  # Add to the overall list
                videos_fps_list.append((file, fps))  # Add to the specific category list
                print(f'Video {file} has {fps} FPS.')

# Set directories
anime_directory = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/anime'
cartoon_directory = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/cartoon'

# List to hold all FPS values
all_fps = []
# Lists to hold titles and FPS values for each category
anime_videos_fps = []
cartoon_videos_fps = []

# Calculate FPS for each set and store the results
average_fps(anime_directory, all_fps, anime_videos_fps)
average_fps(cartoon_directory, all_fps, cartoon_videos_fps)

# Plot FPS distribution for anime and cartoon datasets
plot_fps_for_videos(anime_videos_fps, "Anime")
plot_fps_for_videos(cartoon_videos_fps, "Cartoon")
