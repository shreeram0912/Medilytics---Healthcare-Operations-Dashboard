import streamlit as st
import pandas as pd

df = pd.read_csv(r"C:\Users\Shreeram Prajapati\infosys\month 1\week 3\data.csv")

df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

total_revenue = df['Revenue'].sum()
total_units = df['Units_Sold'].sum()
avg_price = df['Price'].mean()

brand_sales = df.groupby('Brand')['Revenue'].sum().sort_values(ascending=False)
state_sales = df.groupby('State')['Revenue'].sum().sort_values(ascending=False)
segment_units = df.groupby('Segment')['Units_Sold'].sum()

st.title("🚗 Car Sales Dashboard 2025")

#Kpi metrics we are going to show in the top of the dashboard
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Units Sold", total_units)
col3.metric("Average Price", f"₹{avg_price:,.0f}")

st.divider()

st.sidebar.header("Filters")

brand_filter = st.sidebar.selectbox(
    "Select Brand",
    df['Brand'].unique()
)

filtered_df = df[df['Brand'] == brand_filter]

st.subheader(f"Sales Overview for {brand_filter}")

col1, col2 = st.columns(2)

col1.metric(
    "Units Sold",
    filtered_df['Units_Sold'].sum()
)

col2.metric(
    "Revenue",
    f"₹{filtered_df['Revenue'].sum():,.0f}"
)

st.divider()

st.subheader("Revenue by Brand")
st.bar_chart(brand_sales)

st.subheader("Revenue by State")
st.bar_chart(state_sales)

st.subheader("Units Sold by Segment")
st.bar_chart(segment_units)

st.subheader("Dataset Preview")
st.dataframe(df)