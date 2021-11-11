import streamlit as st
import numpy as np
import pandas as pd
import math

st.title("Uber pickups test")

DATA_SOURCE='https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

@st.cache
def download_data():
      datos= (pd.read_csv(DATA_SOURCE).rename(columns={'Lat':'lat', 'Lon':'lon', 'Date/Time':'date'}))
      datos['date'] = pd.to_datetime(datos.date)
      return datos
df= download_data()

slider_hour = st.sidebar.slider('selecciona el rango de hora',0,23, (0,5))

df = df[(df['date'].dt.hour >= min(slider_hour)) & (df['date'].dt.hour <= max(slider_hour))]

page_size=1000
total_pages=math.ceil((len(df)/page_size))
starting_value=0
slider = st.slider('Select the page',1, total_pages )
st.write('page selected',slider,'with limits',(((slider-1)*page_size), (slider*page_size)-1))
pagineo = df.loc[((slider-1)*page_size):(slider*page_size)-1]
pagineo
df['hour'] = df['date'].dt.hour

st.map(pagineo)

st.bar_chart(df['hour'].value_counts())