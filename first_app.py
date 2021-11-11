from itertools import product

import streamlit as st
import numpy as np
import pandas as pd

st.title("This is my first streamlit app, for Galileo Master!")

x = 4
st.write(x, 'square is', x*x)

x, 'square is', x*x

st.write('Now using Dataframes...')

"""
## Data Frames
"""

df = pd.DataFrame({
    'Column A' : [1,2,3,4,5],
    'Column B' : ['A','B','C','D','E'],

})

st.write(df)

"""
# Titulo
## Subtitulo
### Sub sub titulo
"""

df

"""
## Let's use some graphs
"""

chart_df = pd.DataFrame(
    np.random.randn(20, 3),
    columns= ['A','B','C']
)

st.line_chart(chart_df)

"""
## How about a map
"""

map_df = pd.DataFrame(
    np.random.randn(1000, 2) / [50,50] + [37.76, -122.4],
    columns= ['lat','lon']
)

st.map(map_df)

"""
## Show me some widgets
"""

"""
### A checkbox
"""

if st.checkbox('Show me the dataframe'):
    map_df

"""
### slider test
"""

x = st.slider('Select value for x')
st.write(x, 'square is', x*x)

"""
### Options
"""

option = st.selectbox(
    'Which number do you like most?',
    [1,2,3,4,5,6,7,8,9,10]
)

'You selected the option', option

"""
### Progressbar
"""
import time
progress_bar_label= st.empty()
progress_bar = st.progress(0)
progress_bar_2 = st.progress(0)
for i in range(101):
    progress_bar_label.text(f'Iteration {i}')
    progress_bar.progress(i)
    time.sleep(0.1)

for i in range(101):
    progress_bar_2.progress(i)
    time.sleep(0.1)

option_side = st.sidebar.selectbox('Choose your weapon,',[ 'Headgun','Machinegun','Knife'])
st.sidebar.write('Your weapon of choice is:', option_side)

another_slider = st.sidebar.slider('select the range',
                           0.0,100.0 , (25.0,75.0))

st.sidebar.write('the range selected is:', another_slider)