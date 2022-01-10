
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
    st.write (df.head(5))
    
def analyse_europe():
    st.write (df[df['continent'].str.contains("Europe.")])

def analyse_Us():
    st.write (df[df['continent'].str.contains("US.")])

def analyse_Japon():
    st.write (df[df['continent'].str.contains("Japan.")])

if __name__ == "__main__":
    main()

