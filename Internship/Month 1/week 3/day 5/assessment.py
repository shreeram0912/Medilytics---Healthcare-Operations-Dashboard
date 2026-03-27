import pandas as pd

df = pd.read_csv(r"C:\Users\Shreeram Prajapati\infosys\month 1\week 3\data.csv")

chapter_1 = data.head()
print("The story begins with a glimpse of the market:\n", chapter_1)

data.columns = data.columns.str.replace('"', '').str.strip()

chapter_2 = data.shape
print("\nThe market size unfolds:", chapter_2)

chapter_3 = data.columns
print("\nCharacters in our story:", chapter_3)

journey = data.dropna()

chapter_4 = journey.describe()
print("\nThe numbers reveal their secrets:\n", chapter_4)

brands_story = journey.groupby('Brand')['Units_Sold'].sum().sort_values(ascending=False)
print("\nThe strongest brands rise in the story:\n", brands_story.head())

state_story = journey.groupby('State')['Revenue'].sum().sort_values(ascending=False)
print("\nThe richest lands in this journey:\n", state_story.head())

fuel_story = journey.groupby('Fuel_Type')['Units_Sold'].sum().sort_values(ascending=False)
print("\nThe fuels that drive the story:\n", fuel_story)

hero = journey.loc[journey['Revenue'].idxmax()]
print("\nThe hero of our story (highest revenue sale):\n", hero)

top_models = journey.groupby('Model')['Revenue'].sum().sort_values(ascending=False).head()
print("\nThe most celebrated models:\n", top_models)

ending = {
    "total_units_sold": journey['Units_Sold'].sum(),
    "total_revenue": journey['Revenue'].sum(),
    "average_price": journey['Price'].mean()
}

print("\nAnd so the story concludes with its final numbers:\n", ending)