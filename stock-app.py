import streamlit as st
import yfinance as yf
st.title("Stock Price App")
ticker = st.text_input("Enter a stock ticker (e.g. AAPL)")
if ticker:
    data = yf.download(ticker, period="1mo")
    st.line_chart(data["Close"])
    st.write("High:", float(data["Close"].max()))
    st.write("Low:", float(data["Close"].min()))
    st.write("Average:", float(data["Close"].mean()))