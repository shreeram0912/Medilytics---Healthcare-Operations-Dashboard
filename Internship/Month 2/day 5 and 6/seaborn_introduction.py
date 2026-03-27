import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

x = [1,2,3,4,5]
y = [5,7,9,6,10]

categories = ["A","B","C","D"]
values = [10,15,7,20]

data = [10,12,15,20,22,25,25,30,35,40]

box_data = [5,7,8,9,10,12,15,20,22]

heat_data = {
    "A":[1,2,3],
    "B":[4,5,6],
    "C":[7,8,9]
}

df = pd.DataFrame(heat_data)

plt.figure(figsize=(10,8))

plt.subplot(2,3,1)
sns.scatterplot(x=x,y=y)

plt.subplot(2,3,2)
sns.lineplot(x=x,y=y)

plt.subplot(2,3,3)
sns.barplot(x=categories,y=values)

plt.subplot(2,3,4)
sns.histplot(data)

plt.subplot(2,3,5)
sns.boxplot(y=box_data)

plt.subplot(2,3,6)
sns.heatmap(df,annot=True)

plt.tight_layout()
plt.show()