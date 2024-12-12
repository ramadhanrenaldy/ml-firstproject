import streamlit as st
import pandas as pd

st.title('Proyek Pertama Machine Learning')

st.info('App ini digunakan untuk melakukan deployment Machine Learning')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X - Atribut**')
  x = df.drop('species', axis=1)
  x

  st.write('**Y - Kelas**')
  y = df.species
  y
