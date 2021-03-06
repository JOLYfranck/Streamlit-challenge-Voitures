
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
        'analyse_Europe': analyse_Europe,
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
    
    st.write ('-----------------------------------------------------------')

    st.markdown('Voila maintenant un graphique Scatterplot par centimetre cube et chevaux en prenant compte des continents et des poids des vehicules')
    
        
    data = alt.Chart(df).mark_circle().encode(
     x='cubicinches', y='hp', size='weightlbs', color='continent', tooltip=['cubicinches', 'hp', 'weightlbs'])
    
    st.altair_chart(data, use_container_width=True)
    
    
   
    
    st.markdown ('Comme on peut le voir sur ce graphique les US sont predominant en chevaux, poids et centimetre cube.')

    
    
def analyse_Europe():
    
    st.markdown ('En cliquant sur les diffrentes colonnes vous pouvez les classées')
    
    df_europe = (df[df['continent'].str.contains("Europe.")])
    st.write (df_europe.sort_values(by='cubicinches',ascending=False))

    st.write ('-----------------------------------------------------------')

    st.markdown('Voila maintenant un graphique Scatterplot par centimetre cube et chevaux en prenant compte le poids')

    data = alt.Chart(df[df['continent'].str.contains("Europe.")]).mark_circle().encode(
     x='cubicinches', y='hp', size='weightlbs', color='weightlbs', tooltip=['cubicinches', 'hp', 'weightlbs'])

    st.altair_chart(data, use_container_width=True)
    
    st.markdown ('Les vehicules europeen sont tous dans une moyenne ni trop lourd ni trop puissant')

def analyse_Us():
    
    st.markdown ('En cliquant sur les diffrentes colonnes vous pouvez les classées')
    
    df_us = (df[df['continent'].str.contains("US.")])
    st.write (df_us.sort_values(by='cubicinches',ascending=False))

    st.write ('-----------------------------------------------------------')

    st.markdown('Voila maintenant un graphique Scatterplot par centimetre cube et chevaux en prenant compte le poids')

    data = alt.Chart(df[df['continent'].str.contains("US.")]).mark_circle().encode(
     x='cubicinches', y='hp', size='weightlbs', color='weightlbs', tooltip=['cubicinches', 'hp', 'weightlbs'])

    st.altair_chart(data, use_container_width=True)
    
    st.markdown ('Les vehicules americain sont tous dans la demesure en poids, cylindrer, cm3 .... ')

def analyse_Japon():
    
    st.markdown ('En cliquant sur les diffrentes colonnes vous pouvez les classées')
    
    dj_japon = (df[df['continent'].str.contains("Japan.")])
    st.write (dj_japon.sort_values(by='mpg',ascending=True))

    st.write ('-----------------------------------------------------------')

    st.markdown('Voila maintenant un graphique Scatterplot par centimetre cube et chevaux en prenant compte le poids')

    data = alt.Chart(df[df['continent'].str.contains("Japan.")]).mark_circle().encode(
     x='cubicinches', y='hp', size='weightlbs', color='weightlbs', tooltip=['cubicinches', 'hp', 'weightlbs'])

    st.altair_chart(data, use_container_width=True)
    
    
    st.markdown ('Les vehicules japonais sont les plus legers et ceux qui ont un consommation faible')
    
    
if __name__ == "__main__":
    main()

