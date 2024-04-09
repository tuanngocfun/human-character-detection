import re
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the text data from the specified path line by line
file_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/output/dataset.json'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Regular expressions to match the mean_score_prediction and image_id values
score_pattern = r'"mean_score_prediction": (\d+\.\d+)'
id_pattern = r'"image_id": "(\d+)"'

# Extract the values using regex
scores = [float(re.search(score_pattern, line).group(1)) for line in lines if re.search(score_pattern, line)]
image_ids = [re.search(id_pattern, line).group(1) for line in lines if re.search(id_pattern, line)]

# Create a dictionary with image_ids as keys and scores as values
data_dict = {img_id: [] for img_id in set(image_ids)}
for img_id, score in zip(image_ids, scores):
    data_dict[img_id].append(score)

# Calculate standard deviation for each image ID
std_devs = {img_id: np.std(score_list) for img_id, score_list in data_dict.items()}

# Sorting by image ID for better visualization
sorted_ids = sorted(std_devs.keys(), key=lambda x: int(x))
sorted_std_devs = [std_devs[img_id] for img_id in sorted_ids]

sns.set_style("whitegrid")
plt.figure(figsize=(18, 7))
sns.barplot(x=sorted_ids, y=sorted_std_devs, palette='viridis')
plt.xticks(rotation=90)
plt.title('Standard Deviation of Mean Score Predictions for Each Image ID')
plt.xlabel('Image ID')
plt.ylabel('Standard Deviation')
plt.tight_layout()
plt.show()

