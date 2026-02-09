import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Dockerized Data Visualization Dashboard")

data = pd.read_csv("data.csv")

st.subheader("Dataset Preview")
st.dataframe(data)

st.subheader("Monthly Sales Trend")
plt.figure()
plt.plot(data["Month"], data["Sales"], marker='o')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Trend")
st.pyplot(plt)

st.subheader("Monthly Sales Comparison")
plt.figure()
plt.bar(data["Month"], data["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales by Month")
st.pyplot(plt)

st.subheader("Sales Distribution")
plt.figure()
plt.pie(data["Sales"], labels=data["Month"], autopct='%1.1f%%')
plt.title("Sales Distribution")
st.pyplot(plt)
