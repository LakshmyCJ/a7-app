import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import datetime

st.title("Simple Investment Planning App")

# Step 1: User Inputs
st.header("Step 1: Input Your Financial Details")
salary = st.number_input("Enter your monthly salary:", min_value=0, step=1000, key="salary")
monthly_expenses = st.number_input("Enter your expected monthly expenses:", min_value=0, step=500, key="expenses")
investment_amount = st.number_input("Enter the amount you wish to invest in stocks:", min_value=0, step=500, key="investment")

# Calculate Savings
savings = salary - monthly_expenses - investment_amount
st.write(f"Your remaining savings after investment: ₹{savings:.2f}")

# Step 2: Select Companies
st.header("Step 2: Select Companies to Invest In")
tickers = st.text_input("Enter stock tickers (comma-separated, e.g., 'AAPL,GOOGL,MSFT')", "AAPL,GOOGL,MSFT")
tickers_list = [ticker.strip().upper() for ticker in tickers.split(",")]

# Step 3: Fetch Real-Time Stock Data
st.header("Step 3: Fetch Real-Time Stock Data")
@st.cache_data
def fetch_stock_data(tickers):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=365)
    data = {}
    for ticker in tickers:
        df = yf.download(ticker, start=start_date, end=end_date)
        if not df.empty:
            data[ticker] = df['Adj Close']
    return pd.DataFrame(data)

if tickers_list:
    stock_data = fetch_stock_data(tickers_list)
    if not stock_data.empty:
        st.subheader("Historical Stock Prices")
        fig = px.line(stock_data, x=stock_data.index, y=stock_data.columns, title="Stock Price Trends")
        st.plotly_chart(fig)
    else:
        st.warning("No data available for the selected tickers.")

# Step 4: Simple Investment Recommendation
st.header("Step 4: Investment Recommendation")

if investment_amount > 0 and not stock_data.empty:
    st.write("Based on your input, here's a simple investment plan:")
    equal_investment = investment_amount / len(tickers_list)
    for ticker in tickers_list:
        st.write(f"Invest ₹{equal_investment:.2f} in {ticker}.")
else:
    st.write("Please enter a valid investment amount and select companies.")

st.write("This is a simple investment suggestion. For personalized advice, consider consulting a financial expert.")
