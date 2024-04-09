import matplotlib.pyplot as plt

labels = ['Male Characters', 'Female Characters', 'Other/Unspecified Characters']
sizes = [75, 21, 4]  # Assuming 4% are other/unspecified characters
colors = ['blue', 'pink', 'grey']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Gender Disparity in Character Representation')
plt.show()

