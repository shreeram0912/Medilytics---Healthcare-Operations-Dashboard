#piechart
import matplotlib.pyplot as plt

activities = ['eat', 'sleep', 'work', 'play']
slices = [3, 7, 8, 6]

plt.pie(slices, labels = activities, autopct = "%1.1f%%", startangle = 90 )
plt.title("My Daily Activities")
plt.show()

#subplots
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

plt.subplot(1,2,1) # 1 row, 2 columns, first plot
plt.plot(x, y1, marker='o', color = 'blue')
plt.plot(x, y2, marker='o', color = 'orange')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.subplot(1,2,2) # 1 row, 2 columns, second plot
plt.bar(x, y1, color = 'blue', alpha = 0.5, label = 'y1')
plt.bar(x, y2, color = 'orange', alpha = 0.5, label = 'y2') 
plt.title("Bar Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

#adding legends
a=[1, 2, 3, 4, 5]
b=[2, 3, 5, 7, 11]
c=[1, 4, 6, 8, 10]

plt.plot(a,b, label = "Line 1", color = 'blue')
plt.plot(a,c, label = "Line 2", color = 'orange')
plt.title("Line Plot with Legend")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(loc = "upper left")
plt.show()