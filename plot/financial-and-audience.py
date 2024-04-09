import matplotlib.pyplot as plt

# Data for the bar chart
financial_metrics = ['Profit Margin', 'Diversity Increase']
values = [30, 30]  # in percentage

# Creating the bar chart
fig, ax = plt.subplots(figsize=(10, 8))  # Increased figure size for more space
bars = ax.bar(financial_metrics, values, color=['purple', 'orange'], width=0.4)

# Adding value labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval}%', ha='center', va='bottom')

# Setting the title and labels
ax.set_title('Financial & Audience Trends in Animation Industry (Relative to 100%)')
ax.set_ylabel('Percentage (%)')
ax.set_ylim(0, 100)  # Set the y-axis to max out at 100% to represent the full scale

# Adding a note for Streaming Growth
note = "Note: Streaming Growth has been significant, indicating a marked increase in viewership on platforms like Disney+ and Netflix."
plt.figtext(0.5, 0.01, note, ha="center", fontsize=10, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})

# Adjusting layout to accommodate the note
plt.subplots_adjust(bottom=0.15)  # Increased the bottom margin to make space for the note

# Show the plot
plt.show()

