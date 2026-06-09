import streamlit as st
import yfinance as yf
import pandas as pd

st.title("NVDA DataFrame Column Names")

ticker = "NVDA"
st.write(f"Downloading data for {ticker}...")

# Download NVDA data (10 years, daily)
df = yf.download(ticker, period="10y", interval="1d", progress=False)

if df.empty:
    st.error("No data found for NVDA.")
else:
    # Print to Streamlit app
    st.write("Raw DataFrame Columns:")
    st.write(df.columns.tolist())
    st.write("First 5 rows of data:")
    st.write(df.head())

    # Also print to PyCharm console
    print("Raw DataFrame Columns:", df.columns.tolist())
    print("First 5 rows of data:")
    print(df.head())

