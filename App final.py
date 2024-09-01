# Importing necessary libraries
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Title of the app
st.title("Simple Stock Market Investment Planner")

# User inputs for salary, spendings, and investment
salary = st.number_input("Enter your monthly salary:", min_value=0, value=50000, step=1000)
spendings = st.number_input("Enter your expected monthly spendings:", min_value=0, value=20000, step=1000)
investment_amount = st.number_input("Enter your desired investment amount:", min_value=0, value=10000, step=1000)

# Calculate savings
savings = salary - spendings - investment_amount
if savings < 0:
    st.warning("Your spendings and investment exceed your salary. Adjust your values.")
else:
    st.write(f"Your estimated savings for the month: ₹{savings}")

# Fetching real-time stock data
st.subheader("Check Real-Time Stock Data")

# Stock ticker input
ticker = st.text_input("Enter a stock ticker (e.g., AAPL for Apple):", value="AAPL")

# Fetching the stock data using yfinance
if ticker:
    try:
        stock_data = yf.download(ticker, period="1y")
        st.write(f"Displaying data for {ticker}")

        # Show data
        st.write(stock_data.tail())

        # Plot stock price trends
        fig = px.line(stock_data, x=stock_data.index, y="Adj Close", title=f"{ticker} Stock Price Over the Last Year")
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error fetching data for {ticker}. Please check the ticker symbol and try again.")
