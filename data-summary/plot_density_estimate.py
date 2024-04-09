import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

file_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/output/dataset.json'
with open(file_path, 'r') as file:
    lines = file.readlines()

pattern = r'"mean_score_prediction": (\d+\.\d+)'

# Extract the mean_score_prediction values using regex
scores = [float(re.search(pattern, line).group(1)) for line in lines if re.search(pattern, line)]

# Calculate mean and standard deviation
mean_score = np.mean(scores)
std_dev = np.std(scores)

# Generate values for the standard normal distribution
x = np.linspace(mean_score - 4*std_dev, mean_score + 4*std_dev, 1000)
pdf = (1/np.sqrt(2*np.pi*std_dev**2)) * np.exp(-0.5 * ((x - mean_score)/std_dev)**2)

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

plt.plot(x, pdf, color='blue', label='Standard Normal Distribution')

sns.kdeplot(scores, color='purple', label='Kernel Density Estimate of Data')

# Shading the region within 1 standard deviation of the mean
plt.fill_between(x, pdf, where=((x > mean_score - std_dev) & (x < mean_score + std_dev)), color='grey', alpha=0.5, label='68% of Data')

# Vertical lines for mean and standard deviations
plt.axvline(mean_score, color='green', linestyle='--', label='Mean')
plt.axvline(mean_score - std_dev, color='red', linestyle='--', label='-1 SD')
plt.axvline(mean_score + std_dev, color='red', linestyle='--', label='+1 SD')

# Annotations
plt.text(mean_score, plt.gca().get_ylim()[1]*0.05, '68%', fontsize=12, ha='center')

# Labels and title
plt.title('Kernel Density Estimate vs. Standard Normal Distribution')
plt.xlabel('Mean Score Prediction')
plt.ylabel('Density')
plt.legend()

plt.tight_layout()
plt.show()

