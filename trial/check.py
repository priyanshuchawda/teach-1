import matplotlib.pyplot as plt
import numpy as np

# Define the questions/categories
questions = [
    "Avg screen time", "Screen time break", "Sleep impact", 
    "Percentage of screen time", "Screen time for work", 
    "How many Eye strain breaks", "Weekend screen usage", 
    "YT time spend", "Gaming time", "Time spend for study"
]

# Values for Mean, Median, and Mode based on the table
mean_values = [5.96, 4.92, 20.38, 62.69, 76.92, 10.38, 6.38, 5.54, 4.46, 7.15]
median_values = [5.5, 5, 20, 70, 80, 10, 8.5, 7, 6, 6]
mode_values = [9.5, 5, 10, 70, 80, 10, 9, 7, 6, 6]

x = np.arange(len(questions))  # Label locations

# Plotting
width = 0.25  # Width of bars
fig, ax = plt.subplots(figsize=(12, 7))

# Creating bars for Mean, Median, and Mode
bar1 = ax.bar(x - width, mean_values, width, label='Mean')
bar2 = ax.bar(x, median_values, width, label='Median')
bar3 = ax.bar(x + width, mode_values, width, label='Mode')

# Adding labels and titles
ax.set_ylabel('Values')
ax.set_xlabel('Questions')
ax.set_title('Mean, Median, and Mode for Questions')
ax.set_xticks(x)
ax.set_xticklabels(questions, rotation=45, ha="right")
ax.legend()

plt.tight_layout()
plt.show()
