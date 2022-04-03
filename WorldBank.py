import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

# Printing the title of the web app.
st.title('World Bank Data - India')
# Read the csv file
India=pd.read_csv('World_Bank_India.csv',skiprows=4)
st.write(India)
st.write(India.index)
