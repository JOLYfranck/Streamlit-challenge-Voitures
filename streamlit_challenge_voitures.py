import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt



st.title('Challenge Streamlit : build and share data apps')

st.markdown('Voila une analyse de la data Cars.csv')

df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep=',')

st.write (df.head(5))

st.markdown('Comme vous pouvez le voir sur le tableau ci dessus different point sont abordé, petite definition rapide des colonnes')
st.markdown('MPG = Miles par gallon d essence')
st.markdown('cylinders = cylindrée')
st.markdown('cubicinches = inch cube (centimetre cube)')
st.markdown('hp = horse power (cheveaux)')
st.markdown('weightlbs = poids')
st.markdown('time-to-60 = temps pour atteindre les 60 miles')
st.markdown('year = année de production')
st.markdown('continent = pays de production')

st.write ('-----------------------------------------------------------')

st.markdown('Voila maintenant un graphique Heatmap de correlation des données')


correlationheat = sns.heatmap(df.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(correlationheat.figure)



option = st.selectbox('Choisir le continent',('Europe','US','Japan'))


st.write ('Données par continent selectionné :',df[df['continent'].str.contains(option)])


st.markdown ('Si apres vous trouverez different graphiques toujours en rapport avec le continent selectionné')


data = alt.Chart(df[df['continent'].str.contains(option)]).mark_circle().encode(
     x='cubicinches', y='hp', size='weightlbs', color='weightlbs', tooltip=['cubicinches', 'hp', 'weightlbs'])

st.altair_chart(data, use_container_width=True)

