import seaborn as sns
import matplotlib.pyplot as plt

data = [20, 35, 30, 35, 27]
sns.barplot(x=['A', 'B', 'C', 'D', 'E'], y=data)
plt.title('Bar Chart Example')
plt.show()
