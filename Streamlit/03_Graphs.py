import streamlit as st
import pandas as pd
import numpy as np

# working on dataframes
data = pd.read_csv("data.csv")
st.write(data)

# working on charts
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)