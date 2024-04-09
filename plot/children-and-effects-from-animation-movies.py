import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Creating an infographic-style diagram

fig, ax = plt.subplots(figsize=(10, 6))

# Predominance of Male Characters
male_figures = 10
female_figures = 4
ax.barh(['Male Characters'], [male_figures], color='blue', alpha=0.6)
ax.barh(['Female Characters'], [female_figures], color='pink', left=[male_figures], alpha=0.6)

# Stereotypical Roles
male_roles = ['Adventurous', 'Leading', 'Action-Oriented']
female_roles = ['Domestic', 'Passive', 'Supporting']
ax.text(0.5, 0.8, 'Stereotypical Roles:', transform=ax.transAxes, fontsize=12, fontweight='bold')
ax.text(0.5, 0.75, f'Male: {", ".join(male_roles)}', transform=ax.transAxes, fontsize=10)
ax.text(0.5, 0.70, f'Female: {", ".join(female_roles)}', transform=ax.transAxes, fontsize=10)

# Influence on Children's Gender Perception
ax.text(0.5, 0.60, 'Influence on Children:', transform=ax.transAxes, fontsize=12, fontweight='bold')
ax.text(0.5, 0.55, 'Shapes gender role understanding', transform=ax.transAxes, fontsize=10)

# Shifts Over Time
ax.text(0.5, 0.45, 'Shifts Over Time:', transform=ax.transAxes, fontsize=12, fontweight='bold')
ax.text(0.5, 0.40, 'Trend towards more balanced representations', transform=ax.transAxes, fontsize=10)

# Hide axes
ax.axis('off')

# Adding legends
legend_elements = [Patch(facecolor='blue', label='Male Characters'),
                   Patch(facecolor='pink', label='Female Characters')]
ax.legend(handles=legend_elements, loc='lower center')

# Title
plt.title('Gender Representation in Animated Movies', fontsize=14, fontweight='bold')

# Save and display the diagram
plt.savefig('/media/ngoc/mydisk/thesis/important-files/plot/Gender_Representation_Infographic.png')
plt.show()

'/media/ngoc/mydisk/thesis/important-files/plot/Gender_Representation_Infographic.png'

