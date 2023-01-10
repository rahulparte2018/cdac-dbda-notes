import streamlit as st
st.title('This is my first app!')
st.header('This is a header')
st.markdown('Streamlit is **_really_ cool**.')

import pandas as pd
import numpy as np

dataframe = pd.DataFrame(np.random.randn(10, 20),
  columns = ('col %d' % i
    for i in range(20)))
dataframe

dataframe = pd.DataFrame(np.random.randn(10, 5),
  columns = ('col %d' % i
    for i in range(5)))
dataframe
st.write('This is a line_chart.')
st.line_chart(dataframe)

st.write('This is a area_chart.')
st.area_chart(dataframe)

st.write('This is a bar_chart.')
st.bar_chart(dataframe)

st.write('Map data')
data_of_map = pd.DataFrame(
  np.random.randn(1000, 2) / [60, 60] + [36.66, -121.6],
  columns = ['latitude', 'longitude'])
st.map(data_of_map)