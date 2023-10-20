import streamlit as st
st.title("Macro Indicators ")


import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
st.plotly_chart(fig, se_container_width=True)



import plotly.graph_objects as go


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

with st.container():

    fig_1 = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])
    st.plotly_chart(fig_1, se_container_width=True)