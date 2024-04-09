import cv2
import os
import matplotlib.pyplot as plt

def get_video_fps(video_path):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    return fps

def calculate_and_plot_average_fps(directory):
    fps_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                video_path = os.path.join(root, file)
                fps = get_video_fps(video_path)
                fps_list.append(fps)
    
    if fps_list:
        average_fps = sum(fps_list) / len(fps_list)
    else:
        average_fps = 0
    
    return average_fps, len(fps_list)

# Set directories
anime_directory = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/anime'
cartoon_directory = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/cartoon'

# Calculate average FPS for anime and cartoon
anime_avg_fps, anime_count = calculate_and_plot_average_fps(anime_directory)
cartoon_avg_fps, cartoon_count = calculate_and_plot_average_fps(cartoon_directory)

# Calculate the overall average FPS for the entire train set
overall_avg_fps = (anime_avg_fps * anime_count + cartoon_avg_fps * cartoon_count) / (anime_count + cartoon_count)

# Data to plot
categories = ['Anime', 'Cartoon', 'Training Set']
averages = [anime_avg_fps, cartoon_avg_fps, overall_avg_fps]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create bars
ax.bar(categories, averages, color=['blue', 'green', 'orange'])

# Add average FPS as text labels
for i, avg in enumerate(averages):
    ax.text(i, avg, f'{avg:.2f}', ha='center', va='bottom')

# Set title and labels
ax.set_title('Average FPS Comparison')
ax.set_xlabel('Category')
ax.set_ylabel('Average FPS')

# Show the plot
plt.show()
