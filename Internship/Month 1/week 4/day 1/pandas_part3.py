import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Shreeram Prajapati\infosys\month 1\week 3\data.csv")

df['Total_Sales'] = df['Price'] * df['Units_Sold']
df['Profit'] = df['Total_Sales'] * 0.1

car_sales = df.groupby('Model').agg({
    'Total_Sales': 'sum',
    'Units_Sold': 'sum',
    'Profit': 'sum',
    'State': 'nunique',
    'Fuel_Type': 'nunique',
    'Price': 'count'
}).reset_index()

car_sales.columns = ['Model', 'Total_Sales', 'Total_Units', 'Total_Profit', 'Unique_States', 'Unique_Fuel_Types', 'Count']

car_sales['Score'] = car_sales['Total_Units'] + (car_sales['Total_Profit'] / 1000000)

filtered_cars = car_sales[car_sales['Total_Sales'] > 5000000]

sorted_cars = filtered_cars.sort_values(
    by=['Total_Sales', 'Score'],
    ascending=[False, False]
)

print(sorted_cars.head(3))

avg_units = df.groupby('Model')['Units_Sold'].mean().reset_index()

avg_units['Result'] = np.where(
    avg_units['Units_Sold'] > 60,
    'Pass',
    np.where(avg_units['Units_Sold'] > 40, 'Average', 'Poor')
)

result_map = dict(zip(avg_units['Model'], avg_units['Result']))

sorted_cars['Result'] = sorted_cars['Model'].map(result_map)

print(sorted_cars.head(10))