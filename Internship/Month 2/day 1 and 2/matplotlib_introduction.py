import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x, y, color = 'red', linestyle = '--', marker = 'o')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph')
plt.show()

#Bar chart
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
scores = [85, 90, 78, 92, 88]
plt.bar(students, scores, color = 'blue')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.title('Student Scores')
plt.show()

#Bar chart with horizontal bars
plt.barh(students, scores, color = 'green')
plt.xlabel('Scores')
plt.ylabel('Students')
plt.title('Student Scores (Horizontal)')
plt.show()

#Scatter Plot
x = np.random.randint(1,50,100)
y = np.random.randint(1, 100, 100)

plt.scatter( x, y, color = 'purple', marker = 'o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()