
import plotly
import plotly.express as px
import streamlit as st
import pandas as pd

st.title('Working with plotly and streamlit for dashboard')
df = px.data.gapminder()
st.write(df)
st.write(df.columns)
st.write(df.describe())

# data management.
year_option = df['year'].unique().tolist()

year = st.selectbox('which year should we plot?', year_option, 0)

df = df[df['year'] == year]

# plotting
fig = px.scatter(df, x= 'gdpPerap', y ='lifeExp', size='pop', color='country', hover_name='country',
log_x = True, size_max = 55, range_x=[100, 100000], range_y= [20, 90],
animation_frame= 'year', animation_group= 'country')

fig.update_layout(width=1000)
st.write(fig)
    
    