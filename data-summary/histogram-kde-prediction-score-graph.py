import json
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize variables
mean_scores = []

# Extract JSON objects from the file
with open('/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/output/dataset.json', 'r') as f:
    for line in f:
        try:
            # Attempt to parse the line as JSON
            entry = json.loads(line)
            
            # Check if the necessary keys are present
            if 'image_id' in entry and 'mean_score_prediction' in entry:
                mean_scores.append(entry['mean_score_prediction'])
        except json.JSONDecodeError:
            # Ignore the line if it's not valid JSON
            continue

# Plotting the histogram
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.hist(mean_scores, bins=30, color='blue', alpha=0.7)
plt.title("Histogram of mean_score_prediction")
plt.xlabel("Score")
plt.ylabel("Frequency")

# Plotting the KDE
plt.subplot(1,2,2)
sns.kdeplot(mean_scores, shade=True, color='green')
plt.title("KDE of mean_score_prediction")
plt.xlabel("Score")
plt.ylabel("Density")

# Display the plots
plt.tight_layout()
plt.show()

