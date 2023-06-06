# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:31:42 2023

@author: Ashmita
"""
import json
import requests
from streamlit_lottie import st_lottie

import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
        # Simple Stock Price App
        Shown are the stock closing price, Volume and Dividends of Apple!
        
        """)
tickerSymbol = 'AAPL'

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_2xjo7dta.json")

st_lottie(lottie_hello,
          speed=1,
          height= 200,
          width= 200,
          key="hello")




tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period= '1d', start= '2010-5-31', end= '2020-5-31')
# Open 

st.write("""
         ## Closing Price
        """)
    
st.line_chart(tickerDf.Close)

st.write(""" 
         ## Volume
         """)
         
st.line_chart(tickerDf.Volume)


st.write(""" 
         ## Dividends
         
         """)
         
st.line_chart(tickerDf.Dividends)


   

