import matplotlib.pyplot as plt
import numpy as np

# Assuming the global market value is 400 billion in 2023 and grows at a rate of 5% annually
initial_value = 400
growth_rate = 0.05
years = np.arange(2023, 2031)
values = initial_value * (1 + growth_rate) ** (years - 2023)

# Creating a combined figure for both Market Sizes and Annual Growth Rate
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Bar chart for Market Sizes in 2023
market_sizes = [400, 40]  # Global Market and 3D Animation Market
labels = ['Global Market Value', '3D Animation Market']
ax1.bar(labels, market_sizes, color=['teal', 'navy'])
ax1.set_title('Market Sizes in 2023 (in Billion $)')
ax1.set_ylabel('Market Value (Billions $)')

# Line chart for Annual Growth Rate
ax2.plot(years, values, 'o-', color='orange')
ax2.set_title('Annual Growth Rate')
ax2.set_xlabel('Year')
ax2.set_ylabel('Market Value (Billions $)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax2.grid(True)

# Annotate the 5% growth rate on the graph
for i, txt in enumerate(values):
    ax2.annotate(f'{growth_rate*100}%', (years[i], values[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Show the plot
plt.tight_layout()
plt.show()

