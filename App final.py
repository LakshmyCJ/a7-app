import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from pypfopt import EfficientFrontier, risk_models, expected_returns
import datetime

st.title("Simple Portfolio Optimization App")

# Step 3: Select stocks
st.sidebar.header("Select Your Stocks")
stock_list = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NFLX", "NVDA", "PYPL", "ADBE"]
selected_stocks = st.sidebar.multiselect("Select stocks for your portfolio", stock_list, ["AAPL", "MSFT", "GOOGL"])

if not selected_stocks:
    st.error("Please select at least one stock to continue.")
else:
    # Step 4: Fetch historical data
    start_date = st.sidebar.date_input("Start date", datetime.date(2022, 1, 1))
    end_date = st.sidebar.date_input("End date", datetime.date.today())
    data = yf.download(selected_stocks, start=start_date, end=end_date)['Adj Close']

    if data.empty:
        st.error("No data found for the selected date range.")
    else:
        # Step 5: Calculate returns and risk
        st.write(f"Displaying stock data from {start_date} to {end_date}")
        st.line_chart(data)

        # Calculate daily returns
        returns = data.pct_change().dropna()

        # Calculate expected returns and covariance matrix
        mu = expected_returns.mean_historical_return(data)
        S = risk_models.sample_cov(data)

        # Optimize portfolio for max Sharpe ratio
        ef = EfficientFrontier(mu, S)
        weights = ef.max_sharpe()
        cleaned_weights = ef.clean_weights()
        ef.portfolio_performance(verbose=True)

        # Show optimized portfolio
        st.subheader("Optimized Portfolio Weights")
        st.write(cleaned_weights)

        # Step 6: Visualize Efficient Frontier
        st.subheader("Efficient Frontier")

        # Get weights and portfolio returns
        portfolio_df = pd.DataFrame(cleaned_weights.items(), columns=["Stock", "Weight"])
        portfolio_df.set_index("Stock", inplace=True)

        fig = px.bar(portfolio_df, x=portfolio_df.index, y='Weight', title="Portfolio Weights")
        st.plotly_chart(fig)

        # Additional portfolio performance metrics
        expected_annual_return, annual_volatility, sharpe_ratio = ef.portfolio_performance()
        st.write(f"Expected annual return: {expected_annual_return:.2%}")
        st.write(f"Annual volatility: {annual_volatility:.2%}")
        st.write(f"Sharpe Ratio: {sharpe_ratio:.2f}")
