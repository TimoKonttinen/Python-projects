import streamlit as st
import pandas as pd

st.write("""
         # my first app
         
         Hei *tästä se lähtee!*
         """)

df= pd.read_csv("my_data-csv")
st.line_chart(df)