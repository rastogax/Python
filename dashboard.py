# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Sample Dashboard")

data = pd.DataFrame({
    'x': range(10),
    'y': [i**2 for i in range(10)]
})

st.write("Here's a simple line chart:")
st.line_chart(data)

if st.button("Show Data"):
    st.dataframe(data)
