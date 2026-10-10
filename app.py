import streamlit as st
import pandas as pd
from visualization import plot_bar, plot_line, plot_scatter
from ai_helper import get_ai_insights

st.set_page_config(page_title="AI Data Visualization Assistant")

st.title("📊 AI Data Visualization Assistant")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    columns = df.columns.tolist()

    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)

    chart_type = st.selectbox(
        "Select Chart Type",
        ["Bar", "Line", "Scatter"]
    )

    if chart_type == "Bar":
        plot_bar(df, x_axis, y_axis)
    elif chart_type == "Line":
        plot_line(df, x_axis, y_axis)
    elif chart_type == "Scatter":
        plot_scatter(df, x_axis, y_axis)

    if st.button("Get AI Insights"):
        insights = get_ai_insights(df)
        st.write(insights)