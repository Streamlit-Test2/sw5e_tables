import streamlit as st
import pandas as pd
import numpy as np

# Configure page to use wide mode for better display
st.set_page_config(layout="wide")

# Load the data into a DataFrame
df = pd.read_json('force_data.json')

# Streamlit app layout
st.title('Sw5e Force Power Search')

# Create multiple selectboxes for column selection
columns = st.multiselect('Select columns to search:', df.columns)

# Create a dictionary to hold filters
filters = {}

for col in columns:
    unique_values = df[col].dropna().unique()
    unique_values = np.insert(unique_values, 0, 'All')
    selected_value = st.selectbox(f'Select a value from {col}:', options=unique_values, key=col)
    if selected_value != 'All':
        filters[col] = selected_value

# Allow the user to trigger the search
if st.button('Search'):
    results = df
    for col, value in filters.items():
        results = results[results[col] == value]
    # Use st.dataframe to display the results with adjustable settings
    st.dataframe(results, height=600, use_container_width=True)
else:
    st.write('Select columns and values to search.')

# Apply CSS to enable text wrapping in table cells
st.markdown("""
<style>
    .dataframe td {
        white-space: normal !important;
        text-align: left;
        vertical-align: top;
    }
    .stButton > button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)
