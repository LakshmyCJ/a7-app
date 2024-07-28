# investment-app

### Investment Recommendation App: Plan Your Financial Future

#### Overview
The "Investment Recommendation App" is a Streamlit-based tool designed to help users plan their financial future by investing in stocks. By inputting their salary and desired savings percentage, users can determine the amount available for investment. The app then uses tickers from a Kaggle CSV file to provide detailed stock information and investment recommendations, leveraging historical stock data from Yahoo Finance.

#### Key Features

1. **User Inputs**:
   - **Salary Input**: Users can input their monthly salary.
   - **Savings Slider**: A slider allows users to select the percentage of their salary they wish to save, helping calculate the amount available for investment.

2. **Stock Selection**:
   - **Company Selection**: Users can select up to 10 companies from the Nifty 500 list to include in their investment portfolio. The app uses tickers from a Kaggle dataset for these selections.

3. **Data Retrieval**:
   - **Stock Data**: The app retrieves historical stock price data for the selected companies from Yahoo Finance, spanning the last two years.

4. **Portfolio Optimization**:
   - **Expected Returns and Covariance**: The app calculates expected returns and the covariance matrix for the selected stocks.
   - **Efficient Frontier**: Using the `pypfopt` library, the app optimizes the portfolio to maximize the Sharpe ratio, providing a balanced mix of risk and return.
   - **Performance Metrics**: Users can view the optimized portfolio weights, expected annual return, annual volatility, and Sharpe ratio.

5. **Visualization**:
   - **Historical Stock Prices**: The app provides an interactive line chart to explore historical stock prices for the selected companies using Plotly.

#### Summary
The app is a comprehensive tool for financial planning and investment, offering users the ability to:
- Determine available funds for investment based on their salary and savings.
- Select preferred stocks from a reliable dataset.
- Retrieve and analyze historical stock data.
- Optimize their investment portfolio for maximum returns and minimal risk.
- Visualize historical price trends for informed decision-making.

By combining user inputs, data retrieval, financial analysis, and visualization, the app serves as an all-in-one platform for personal investment planning.
