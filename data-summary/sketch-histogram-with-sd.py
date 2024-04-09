import re
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the text data from the specified path line by line
file_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/output/dataset.json'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Regular expression to match the mean_score_prediction values
pattern = r'"mean_score_prediction": (\d+\.\d+)'

# Extract the mean_score_prediction values using regex
scores = [float(re.search(pattern, line).group(1)) for line in lines if re.search(pattern, line)]

# Calculate mean and standard deviation
mean_score = np.mean(scores)
std_dev = np.std(scores)

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

sns.histplot(scores, bins=30, color='skyblue', edgecolor='black', alpha=0.7, label='Histogram')

# Mean and SD lines
plt.axvline(mean_score, color='green', linestyle='--', label='Mean')
plt.axvline(mean_score - std_dev, color='red', linestyle='--', label='-1 SD')
plt.axvline(mean_score + std_dev, color='red', linestyle='--', label='+1 SD')

plt.title('Distribution of Mean Score Predictions')
plt.xlabel('Mean Score Prediction')
plt.ylabel('Number of Images')
plt.legend()
plt.tight_layout()
plt.show()

