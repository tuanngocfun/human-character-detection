import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from scipy.stats import norm

file_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/output/dataset.json'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Regular expression to match the mean_score_prediction values
pattern = r'"mean_score_prediction": (\d+\.\d+)'

# Extract the mean_score_prediction values using regex
scores = [float(re.search(pattern, line).group(1)) for line in lines if re.search(pattern, line)]

mean_score = np.mean(scores)
std_dev = np.std(scores)

# Determine percentage of scores within one standard deviation
within_one_sd = [score for score in scores if mean_score - std_dev <= score <= mean_score + std_dev]
percentage_within_one_sd = len(within_one_sd) / len(scores) * 100

# Kernel Density Estimate for the dataset
x = np.linspace(min(scores), max(scores), 1000)
pdf = norm.pdf(x, mean_score, std_dev)

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

sns.kdeplot(scores, color='purple', label='Kernel Density Estimate of Data')

# Shading the region within 1 standard deviation of the mean
plt.fill_between(x, pdf, where=((x > mean_score - std_dev) & (x < mean_score + std_dev)), color='grey', alpha=0.5, label=f'{percentage_within_one_sd:.2f}% of Data')

# Vertical lines for mean and standard deviations
plt.axvline(mean_score, color='green', linestyle='--', label='Mean')
plt.axvline(mean_score - std_dev, color='red', linestyle='--', label='-1 SD')
plt.axvline(mean_score + std_dev, color='red', linestyle='--', label='+1 SD')

# Annotations
plt.text(mean_score, plt.gca().get_ylim()[1]*0.05, f'{percentage_within_one_sd:.2f}%', fontsize=12, ha='center')

plt.title('Kernel Density Estimate and Data within 1 SD')
plt.xlabel('Mean Score Prediction')
plt.ylabel('Density')
plt.legend()

plt.tight_layout()
plt.show()

