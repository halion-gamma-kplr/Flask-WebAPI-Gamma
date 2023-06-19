import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv('Citizen_DATA.csv')
st.line_chart(df.iloc[5:20],x='id',y='age')
st.area_chart(df.iloc[5:20],x='id',y='age')
st.bar_chart(df.iloc[5:20],x='id',y='age')

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)

st.pyplot(plt)

fig = px.funnel(df.iloc[5:20], x='city', y='age') 
st.plotly_chart(fig)

st.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'age', 'type': 'quantitative'},
        'y': {'field': 'id', 'type': 'quantitative'},
        'size': {'field': 'age', 'type': 'quantitative'},
        'color': {'field': 'id', 'type': 'quantitative'},
    },
})