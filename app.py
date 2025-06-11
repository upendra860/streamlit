import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Sample ETF Swing Trading Dashboard")

# Dummy OHLC data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10),
    'Open': np.random.uniform(100, 200, 10),
    'High': np.random.uniform(200, 250, 10),
    'Low': np.random.uniform(90, 150, 10),
    'Close': np.random.uniform(100, 200, 10)
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Display data
st.subheader("📊 OHLC Data")
st.dataframe(df)

# Simple moving average chart
st.subheader("📉 Close Price with Moving Average")
window = st.slider("SMA Window", min_value=2, max_value=10, value=3)
df['SMA'] = df['Close'].rolling(window=window).mean()
st.line_chart(df[['Close', 'SMA']])
