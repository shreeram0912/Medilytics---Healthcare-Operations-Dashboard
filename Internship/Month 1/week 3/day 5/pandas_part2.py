import pandas as pd

df = pd.read_csv(r"C:\Users\Shreeram Prajapati\infosys\month 1\week 3\data.csv")

print(df.head())
df.columns = df.columns.str.replace('"' , '').str.strip()
print(df.columns)

df.shape

df.columns

df.info()

df.describe()

df['Brand']

df.iloc[0]

df.iloc[0:4]