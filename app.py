import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


st.set_page_config(page_title="Data Visualizer Dashboard", layout="wide")

st.title("Data Visualization Dashboard")
st.markdown("Upload any CSV file")

st.sidebar.header("Controls")

uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    
    data = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(data)

    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = data.select_dtypes(include=['object']).columns.tolist()

    st.sidebar.subheader("Chart Settings")
    
    x_col = st.sidebar.selectbox("Select X-axis", data.columns)
    y_col = st.sidebar.selectbox("Select Y-axis", numeric_cols)

    chart_type = st.sidebar.selectbox(
        "Chart Type",
        ["Line", "Bar", "Scatter", "Pie"]
    )

    st.sidebar.subheader("Filter Data")

    use_filter = st.sidebar.checkbox("Enable Filter")

    if use_filter and categorical_cols:
        filter_col = st.sidebar.selectbox("Filter Column", categorical_cols)
        filter_val = st.sidebar.selectbox(
            "Select Value",
            data[filter_col].unique()
        )
        data = data[data[filter_col] == filter_val]

    elif use_filter and not categorical_cols:
        st.sidebar.warning("No categorical columns available for filtering")

    st.subheader("Key Metrics")
    
    col1, col2, col3 = st.columns(3)

    if numeric_cols:
        col1.metric("Total", int(data[y_col].sum()))
        col2.metric("Average", round(data[y_col].mean(), 2))
        col3.metric("Max", int(data[y_col].max()))

    if x_col != y_col:
        grouped_data = data.groupby(x_col)[y_col].sum().reset_index()
    else:
        grouped_data = data.copy()

    st.subheader("Visualization")
    fig, ax = plt.subplots()

    if chart_type == "Line":
        ax.plot(grouped_data[x_col], grouped_data[y_col], marker='o')

    elif chart_type == "Bar":
        ax.bar(grouped_data[x_col], grouped_data[y_col])

    elif chart_type == "Scatter":
        ax.scatter(data[x_col], data[y_col])

    elif chart_type == "Pie":
        ax.pie(grouped_data[y_col], labels=grouped_data[x_col], autopct='%1.1f%%')

    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f"{y_col} vs {x_col}")

    st.pyplot(fig)

    if len(numeric_cols) >= 2:
        st.subheader("Extra Insight: Scatter Between Numeric Columns")
        fig2, ax2 = plt.subplots()
        ax2.scatter(data[numeric_cols[0]], data[numeric_cols[1]])
        ax2.set_xlabel(numeric_cols[0])
        ax2.set_ylabel(numeric_cols[1])
        st.pyplot(fig2)

else:
    st.info("Upload a CSV file from the sidebar to get started")