import pandas as pd

# Load the dataset
data = pd.read_csv('Global_Superstore.csv', encoding='ISO-8859-1')

# Display basic info
print(data.head())
print(data.info())

# Data cleaning (if needed)
data.dropna(subset=['Sales', 'Profit', 'Category', 'Sub-Category'], inplace=True)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset
data = pd.read_csv('Global_Superstore.csv', encoding='ISO-8859-1')

# Dashboard Title
st.title("Global Superstore Sales Dashboard")

# Total Accounts Receivable
total_accounts_receivable = data['Sales'].sum()
st.metric(label="Total Sales", value=f"${total_accounts_receivable:,.2f}")

# Total Amounts Payable
total_amounts_payable = data['Profit'].sum()
st.metric(label="Total Profit", value=f"${total_amounts_payable:,.2f}")

# Add a section for visualizations
st.header("Sales and Profit Analysis")

# Sales by Category
category_sales = data.groupby('Category')['Sales'].sum().reset_index()
fig1 = px.bar(category_sales, x='Category', y='Sales', title='Sales by Category')
st.plotly_chart(fig1)

# Profit by Category
category_profit = data.groupby('Category')['Profit'].sum().reset_index()
fig2 = px.bar(category_profit, x='Category', y='Profit', title='Profit by Category')
st.plotly_chart(fig2)

# Sales Trend Over Time
data['Order Date'] = pd.to_datetime(data['Order Date'])
sales_trend = data.groupby(data['Order Date'].dt.to_period("M"))['Sales'].sum().reset_index()
sales_trend['Order Date'] = sales_trend['Order Date'].dt.to_timestamp()

fig3, ax = plt.subplots()
ax.plot(sales_trend['Order Date'], sales_trend['Sales'], marker='o')
ax.set_title('Sales Trend Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
st.pyplot(fig3)

# Display additional KPIs
st.header("Key Performance Indicators")
st.metric(label="Equity Ratio", value="75.38%")
st.metric(label="Debt Equity", value="1.10%")