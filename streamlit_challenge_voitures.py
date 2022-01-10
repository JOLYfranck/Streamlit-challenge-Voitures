import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

st.title('Challenge Streamlit : build and share data apps')

df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep=',')

option = st.selectbox('Continent',('Europe','US','Japan'))
st.write ('Données par continent selectioné :',df[df['continent'].str.contains(option)])


data = alt.Chart(df[df['continent'].str.contains(option)]).mark_circle().encode(
     x='cubicinches', y='hp', size='weightlbs', color='weightlbs', tooltip=['cubicinches', 'hp', 'weightlbs'])

st.altair_chart(data, use_container_width=True)