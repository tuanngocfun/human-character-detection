import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def plot_and_show_stats(directory):
    sizes = [Image.open(os.path.join(directory, file)).size for file in os.listdir(directory) if file.endswith('.jpg')]
    widths, heights = zip(*sizes)

    # Calculate statistics for widths
    mean_width = np.mean(widths)
    median_width = np.median(widths)
    std_width = np.std(widths)

    # Calculate statistics for heights
    mean_height = np.mean(heights)
    median_height = np.median(heights)
    std_height = np.std(heights)

    print(f"Statistics for {directory}:")
    print(f"Width - Mean: {mean_width}, Median: {median_width}, Std: {std_width}")
    print(f"Height - Mean: {mean_height}, Median: {median_height}, Std: {std_height}")

    # Plotting the graph
    plt.scatter(widths, heights)
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.title(f'Image Size Distribution in {directory}')
    plt.show()

plot_and_show_stats('/home/aivn12gb/yolov8_domain_adaption_evn/data/new-val/images')