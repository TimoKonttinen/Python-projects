import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
         #yksinkertainen osakehinta-applikaatio
         Sovellus näyttää päätöskurssit ja volyymit Googlen tietokannasta
         Näytön voi myös vaihtaa muille osakkeille""" 
         )

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDF= tickerData.history(period='1d', start='2010-5-31', end= '2022-9-9')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)