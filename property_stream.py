import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode

def flatten_column_to_set(series):
    flat_set = set()
    for item in series:
        if isinstance(item, list):
            flat_set.update(item)
        else:
            flat_set.add(item)
    return sorted(list(flat_set))
# Configure page to use wide mode for better display
st.set_page_config(layout="wide")

# Load the data into a DataFrame
df = pd.read_json('allProperty.json')
df.sort_values('name')

# Streamlit app layout
st.title('Sw5e Property Search')

# Create multiple selectboxes for column selection
columns = st.multiselect('Select columns to search:', ["name", "type"])

# Create a dictionary to hold filters
filters = {}

for col in columns:
    if df[col].apply(lambda x: isinstance(x, list)).any():
        # Handle list-containing columns
        unique_values = flatten_column_to_set(df[col].dropna())
        unique_values = ['All'] + list(unique_values)
    else:
        # Normal handling for non-list columns
        unique_values = df[col].dropna().unique()
        unique_values.sort()
        unique_values = np.insert(unique_values, 0, 'All')
    
    selected_value = st.selectbox(f'Select a value from {col}:', options=unique_values, key=col)
    if selected_value != 'All':
        if isinstance(df[col].iloc[0], list):
            # Filter handling for list columns
            filters[col] = lambda df, col=col, selected_value=selected_value: df[col].apply(lambda x: selected_value in x)
        else:
            # Normal filter handling
            filters[col] = selected_value

# Allow the user to trigger the search
if st.button('Search'):
    results = df
    for col, value in filters.items():
        if callable(value):
            # Apply the lambda filter for list columns
            results = results[value(results) == True]
            
            
        else:
            # Standard filtering
            results = results[results[col] == value]
    # Use st.dataframe to display the results with adjustable settings
    #st.dataframe(results, height=600, use_container_width=True)
else:
    st.write('Select columns and values to search.')
    results = df


#builds a gridOptions dictionary using a GridOptionsBuilder instance.
builder = GridOptionsBuilder.from_dataframe(df)
builder.configure_column("name",flex=1)
builder.configure_column("content", cellStyle={'whiteSpace': 'normal'}, autoHeight=True, flex=1, maxWidth=1350)
builder.configure_column("type",flex=1)
#builder.autoSizeStrategy(type = 'fitGridWidth')
go = builder.build()
# Configure column definitions for manual width adjustments

grid_response = AgGrid(
    results,
    fit_columns_on_grid_load=False,  # Turn off auto-fitting to allow manual size adjustments
    theme='alpine',
    allow_unsafe_jscode=True,        # Required to enable some advanced features
    enable_enterprise_modules=True,  # Enable enterprise features
    height=600,                      # Set the grid height
    width='90%',                    # Set the grid width
    gridOptions = go, 
)