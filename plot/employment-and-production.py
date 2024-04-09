import matplotlib.pyplot as plt

# Data for the Employment & Production
job_growth = 30  # in percentage
cga_market_share = 85  # in percentage for Computer-Generated Animation
other_animation_market_share = 15  # in percentage for other types of animation

# Creating the bar chart for Job Growth
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Bar chart for Job Growth in the Animation Industry
axs[0].bar(['Job Growth'], [job_growth], color='orange')
axs[0].set_title('Job Growth in Animation Industry (in %)')
axs[0].set_ylim(0, 100)  # Percentage scale
axs[0].set_ylabel('Growth %')

# Pie chart for Animation Market Share
axs[1].pie([cga_market_share, other_animation_market_share], 
           labels=['CGA Dominance', 'Other Animation'], 
           autopct='%1.1f%%', startangle=90, 
           colors=['lightblue', 'lightgrey'])
axs[1].set_title('Animation Market Share (in %)')

# Show the plot
plt.tight_layout()
plt.show()

