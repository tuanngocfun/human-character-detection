import matplotlib.pyplot as plt

# Global market size
global_market_size = 400  # in billions of dollars

# Assuming North America takes about 50% of the global market
north_america_market_size = global_market_size * 0.5

# Asia Pacific market size based on Japan and China's markets
asia_pacific_market_size = 18 + 34  # in billions of dollars

# Remaining market size for Europe & Latin America
remaining_market_size = global_market_size - (north_america_market_size + asia_pacific_market_size)

# Recalculated regional market sizes
regions = ['North America', 'Asia Pacific', 'Europe & Latin America']
market_values_recalculated = [north_america_market_size, asia_pacific_market_size, remaining_market_size]

# Plotting the corrected regional market sizes bar chart
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(regions, market_values_recalculated, color=['navy', 'darkgreen', 'purple'])
ax.set_title('Regional Animation Market Sizes in 2023 (in Billion $)')
ax.set_ylabel('Market Value (Billions $)')
ax.set_ylim(0, max(market_values_recalculated) * 1.1)  # Set y-limit to be a bit higher than the max value

# Adding the actual values above the bars for clarity
for i, v in enumerate(market_values_recalculated):
    ax.text(i, v + 10, f"${v}B", color='black', ha='center')

# Show the plot
plt.show()

