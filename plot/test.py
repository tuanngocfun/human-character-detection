import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Technique': ['Raw Extract Frame', 'Single (x1) Hash Difference', 'Hash Difference then Cosine Similarity', 
                  'Single (x1) Cosine Similarity', 'Double (x2) Cosine Similarity'],
    'Anime': [1858715, 73762, 16277, 46694, 15317],
    'Cartoon': [883129, 42416, 13916, 26203, 9998]
}

df = pd.DataFrame(data)

# Set the index to 'Technique' for better plotting
df.set_index('Technique', inplace=True)

# Bar chart for direct comparison
df.plot(kind='bar', figsize=(10, 7))
plt.title('Comparison of Image Counts After Preprocessing')
plt.ylabel('Number of Images')
plt.xlabel('Preprocessing Technique')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Line chart to show trends over different techniques
df.plot(kind='line', figsize=(10, 7), marker='o')
plt.title('Trend of Image Counts After Preprocessing')
plt.ylabel('Number of Images')
plt.xlabel('Preprocessing Technique')
plt.grid(True)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()
