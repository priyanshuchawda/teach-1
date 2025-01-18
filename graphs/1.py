import matplotlib.pyplot as plt

labels = ['Python', 'C++', 'Java', 'JavaScript']
sizes = [215, 130, 245, 210]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.title("Programming Language Popularity")
plt.show()
