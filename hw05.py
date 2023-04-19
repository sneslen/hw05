import pandas as pd
import plotly.express as px
import streamlit as st

url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'

df = pd.read_csv(url)

st.title('Name Plot')

pattern = st.text_input('Type a name to search', placeholder = 'Enter a name or regular expression.')

name_df = df[df['name']==pattern]

fig = px.scatter(name_df, x='year',y='n', color='sex')
fig.update_layout(title=f'Name Trend for {pattern} from 1910-2021')

st.plotly_chart(fig)
