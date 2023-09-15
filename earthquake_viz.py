import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import altair as alt

st.title('Global Earthquakes in the Last 7 Days')

# Fetch the data from USGS
DATA_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv"

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    data['time'] = pd.to_datetime(data['time'])
    return data

data = load_data()

# Allow users to view raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Histogram of earthquake magnitudes
st.subheader('Distribution of Earthquake Magnitudes')
hist_values = np.histogram(data['mag'], bins=30, range=(0,10))[0]
st.bar_chart(hist_values)

# Filter earthquakes by magnitude
magnitude_to_filter = st.slider('Filter by minimum magnitude', 0.0, 10.0, 5.0)
filtered_data = data[data['mag'] >= magnitude_to_filter]

st.subheader(f'Map of all Earthquakes with magnitude > {magnitude_to_filter}')
map_click = st.map(filtered_data[['latitude', 'longitude']].dropna(how="any"), zoom=1)

# Time series analysis
st.subheader('Earthquake Frequency Over Time')
fig, ax = plt.subplots(figsize=(10,5))
data['time'].dt.date.value_counts().sort_index().plot(kind='line', ax=ax)
st.pyplot(fig)

# Magnitude vs. Depth scatter plot
st.subheader('Magnitude vs. Depth of Earthquakes')
chart = alt.Chart(data).mark_circle().encode(
    x='depth:Q',
    y='mag:Q',
    tooltip=['mag', 'depth', 'place', 'time']
).properties(width=700, height=400)
st.altair_chart(chart)

# Top 5 earthquakes
st.subheader('Top 5 Earthquakes by Magnitude')
top_quakes = data.nlargest(5, 'mag')
st.write(top_quakes)
