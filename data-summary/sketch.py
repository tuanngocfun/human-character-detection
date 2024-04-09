import re
import matplotlib.pyplot as plt
import seaborn as sns

# Read the text data from the specified path line by line
file_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/output/dataset.json'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Regular expression to match the mean_score_prediction values
pattern = r'"mean_score_prediction": (\d+\.\d+)'

# Extract the mean_score_prediction values using regex
scores = [float(re.search(pattern, line).group(1)) for line in lines if re.search(pattern, line)]

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Histogram
sns.histplot(scores, bins=30, kde=True, color='skyblue', edgecolor='black', alpha=0.7, label='Histogram')

# KDE
sns.kdeplot(scores, color='red', lw=2, label='KDE')

plt.title('Distribution of Mean Score Predictions')
plt.xlabel('Mean Score Prediction')
plt.ylabel('Number of Images')
plt.legend()
plt.tight_layout()
plt.show()

