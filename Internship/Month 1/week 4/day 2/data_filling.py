import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Shreeram Prajapati\infosys\month 1\week 3\data.csv")

df.loc[2, 'Price'] = None

df.isnull().sum()

df.fillna(df.mean(numeric_only = True ,inplace=True))

print(df)

df.dropna(inplace=True)