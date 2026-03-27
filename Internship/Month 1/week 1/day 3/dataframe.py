import pandas as pd

data = {
    "name" : ["Alice", "Bob", "Charlie"],
    "salary" : [25000, 30000, 35000]
}

df = pd.DataFrame(data)

average_salary = df['salary'].mean()
print("Average salary:", average_salary)