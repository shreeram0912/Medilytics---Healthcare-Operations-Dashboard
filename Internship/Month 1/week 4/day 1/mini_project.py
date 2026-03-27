import pandas as pd
import numpy as np

#task1 - correct mapping logic,2 - have to handle missing data by generating own data and outside data also 

data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [25, np.nan, 30, 22, np.nan],
    'Salary': [50000, 60000, np.nan, 45000, 52000],
    'Department': ['HR', 'IT', 'HR', np.nan, 'Finance']
}

df1 = pd.DataFrame(data)

df1['Age'] = df1['Age'].fillna(df1['Age'].mean())
df1['Salary'] = df1['Salary'].fillna(df1['Salary'].mean())
df1['Department'] = df1['Department'].fillna(df1['Department'].mode()[0])

dept_mapping = {'HR': 1, 'IT': 2, 'Finance': 3}
df1['Dept_Code'] = df1['Department'].map(dept_mapping)

df2 = pd.read_csv("C:/Users/SaiTej Barla/Downloads/Iris.csv")

np.random.seed(0)
for col in df2.columns[1:-1]:
    df2.loc[df2.sample(frac=0.1).index, col] = np.nan

num_cols = df2.select_dtypes(include=np.number).columns
for col in num_cols:
    df2[col] = df2[col].fillna(df2[col].mean())

df2['Species'] = df2['Species'].fillna(df2['Species'].mode()[0])

species_mapping = {
    'Iris-setosa': 1,
    'Iris-versicolor': 2,
    'Iris-virginica': 3,
    'setosa': 1,
    'versicolor': 2,
    'virginica': 3
}

df2['Species_Code'] = df2['Species'].map(species_mapping)

print(df1)
print(df2.head())