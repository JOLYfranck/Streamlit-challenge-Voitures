import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

st.title('Challenge Streamlit : build and share data apps')

st.markdown('Voila une analyse de la data Cars.csv')

df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep=',')

st.write (df.head(10))

st.markdown('Comme vous pouvez le voir sur le tableau ci dessus different point sont abordé, petite definition rapide des colonnes')

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

