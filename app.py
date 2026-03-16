import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Automatic CSV Data Visualization Dashboard")

st.write("Upload any CSV file and generate charts automatically.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    
    data = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(data)

    columns = data.columns.tolist()

    st.subheader("Select Columns for Visualization")

    x_column = st.selectbox("Select X-axis", columns)
    y_column = st.selectbox("Select Y-axis", columns)

    chart_type = st.selectbox(
        "Select Chart Type",
        ["Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart"]
    )

    fig, ax = plt.subplots()

    if chart_type == "Line Chart":
        ax.plot(data[x_column], data[y_column], marker='o')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title(f"{y_column} vs {x_column}")

    elif chart_type == "Bar Chart":
        ax.bar(data[x_column], data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title(f"{y_column} vs {x_column}")

    elif chart_type == "Scatter Plot":
        ax.scatter(data[x_column], data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title(f"{y_column} vs {x_column}")

    elif chart_type == "Pie Chart":
        ax.pie(data[y_column], labels=data[x_column], autopct='%1.1f%%')
        ax.set_title(f"{y_column} Distribution")

    st.pyplot(fig)