
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import altair as alt



df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep=',')




def main():
    
    pages = {
        'Home': homepage,
        'analyse_europe': analyse_europe,
        'analyse_Us': analyse_Us,
        'analyse_Japon': analyse_Japon}

    if "page" not in st.session_state:
        st.session_state.update({
        # Default page
        'page': 'Home'
        })

    with st.sidebar:
        page = st.selectbox("Choose a page", tuple(pages.keys()))

    pages[page]()



def homepage():
    st.markdown('Voila une analyse de la data Cars.csv')
    
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
    
    
def analyse_europe():
    st.write (df[df['continent'].str.contains("Europe.")])

    data = alt.Chart(df[df['continent'].str.contains("Europe.")]).mark_circle().encode(
     x='cubicinches', y='hp', size='weightlbs', color='weightlbs', tooltip=['cubicinches', 'hp', 'weightlbs'])

    st.altair_chart(data, use_container_width=True)


def analyse_Us():
    df_us = (df[df['continent'].str.contains("US.")])
    st.write (df_us.head(5))

    data = alt.Chart(df[df['continent'].str.contains("US.")]).mark_circle().encode(
     x='cubicinches', y='hp', size='weightlbs', color='weightlbs', tooltip=['cubicinches', 'hp', 'weightlbs'])

    st.altair_chart(data, use_container_width=True)

def analyse_Japon():
    st.write (df[df['continent'].str.contains("Japan.")])

    data = alt.Chart(df[df['continent'].str.contains("Japan.")]).mark_circle().encode(
     x='cubicinches', y='hp', size='weightlbs', color='weightlbs', tooltip=['cubicinches', 'hp', 'weightlbs'])

    st.altair_chart(data, use_container_width=True)

if __name__ == "__main__":
    main()

