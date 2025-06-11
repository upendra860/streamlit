# app.py
import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 Live OHLC Data Viewer")

# User input
ticker = st.text_input("Enter ETF ticker (e.g., GOLDBEES.NS)", value="GOLDBEES.NS")
period = st.selectbox("Select period", ["5d", "1mo", "3mo", "6mo", "1y"], index=1)
interval = st.selectbox("Select interval", ["1d", "1h", "15m"], index=0)

# Fetch data
if ticker:
    df = yf.download(ticker, period=period, interval=interval)
    
    if not df.empty:
        st.subheader("📊 OHLC Data")
        st.dataframe(df.tail())

        st.subheader("📉 Close Price with SMA")
        sma_window = st.slider("SMA Window", min_value=2, max_value=20, value=5)
        df['SMA'] = df['Close'].rolling(window=sma_window).mean()

        st.line_chart(df[['Close', 'SMA']])
    else:
        st.warning("No data found. Try another symbol or increase the period.")
