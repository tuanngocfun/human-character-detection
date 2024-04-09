import matplotlib.pyplot as plt

categories = ['raw extract frame', 'single hash difference', 'hash difference then cosine similarity', 
              'single(x1) cosine similarity']
anime_counts = [1858715, 73762, 16277, 46694]
cartoon_counts = [883129, 42416, 13916, 26203]

# categories = ['raw extract frame', 'single hash difference', 'hash difference then cosine similarity', 
#               'single(x1) cosine similarity', 'double(x2) cosine similarity']
# anime_counts = [1858715, 73762, 16277, 46694, 15317]
# cartoon_counts = [883129, 42416, 13916, 26203, 9998]

# Define the width of the bars
bar_width = 0.35

# Set up the figure size and resolution
plt.figure(figsize=(10, 8), dpi=80)

# Set the positions of the bars on the x-axis
r1 = range(len(categories))
r2 = [x + bar_width for x in r1]

# Create the bar charts
plt.bar(r1, anime_counts, color='blue', width=bar_width, edgecolor='gray', label='Anime')
plt.bar(r2, cartoon_counts, color='orange', width=bar_width, edgecolor='gray', label='Cartoon')

# Add the category names to the x-axis
plt.xlabel('Preprocessing Techniques', fontweight='bold')
plt.xticks([r + bar_width/2 for r in range(len(categories))], categories, rotation=45, ha="right")

# Add a title and a y-axis label
plt.title('Dataset Distribution Across Different Preprocessing Techniques')
plt.ylabel('Number of Images')

plt.legend()

plt.tight_layout()
plt.show()

