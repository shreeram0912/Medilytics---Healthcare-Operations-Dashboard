import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.normal(0,1,100)
data2 = np.random.normal(1,1,100)

#bar chart
plt.bar(data1, data2, color = 'orange', linestyle = '--')
plt.xlabel('data1')
plt.ylabel('data2')
plt.title('Bar Chart')
plt.show()

#horizontal bar chart
plt.barh(data1, data2, color = 'cyan', linestyle = '--')
plt.xlabel('data2')
plt.ylabel('data1')
plt.title('Horizontal Bar Chart')
plt.show()

#scatter plot
plt.scatter(data1, data2, color = 'red')
plt.xlabel('data1')
plt.ylabel('data2')
plt.title('Scatter Plot')
plt.show()