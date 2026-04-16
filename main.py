from dotenv import load_dotenv
import os

load_dotenv()
import pandas as pd
from src.data_loader import fetch_stock_data
from src.data_loader import fetch_interest_rates
from src.analysis import calculate_returns, calculate_risk_return, correlation_matrix
from src.analysis import find_optimal_portfolio
from src.analysis import generate_random_portfolios
from src.visualization import plot_efficient_frontier
from src.visualization import plot_performance, plot_correlation, plot_risk_return
from src.visualization import plot_interest_vs_returns

# Step 1: Define stocks
stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "^GSPC"]  # Comparing stocks with  S&P 500 Index

# Step 2: Fetch data
data = fetch_stock_data(stocks, "2018-01-01", "2024-01-01")

# Fetch interest rates

import os
api_key = os.getenv("FRED_API_KEY")
interest_rates = fetch_interest_rates(api_key)
print("\nInterest Rate Data:")
print(interest_rates.tail())

# Step 3: Analysis
returns = calculate_returns(data)

# Align interest rates with stock returns dates
interest_rates = interest_rates.to_frame(name="Interest_Rate")

# Convert index to datetime (important)
interest_rates.index = pd.to_datetime(interest_rates.index)
returns.index = pd.to_datetime(returns.index)

# Merge datasets
merged_data = returns.join(interest_rates, how="inner")

print("\nMerged Data:")
print(merged_data.head())

print("\nCorrelation with Interest Rates:")
print(merged_data.corr()["Interest_Rate"])

risk, mean_return = calculate_risk_return(returns)
corr = correlation_matrix(returns)

# Step 4: Visualization
plot_performance(data)
plot_correlation(corr)
plot_risk_return(risk, mean_return)
plot_interest_vs_returns (merged_data)

# Step 5: Portfolio Optimization
results = generate_random_portfolios(5000, returns)
best = find_optimal_portfolio(results)

plot_efficient_frontier(results,best)

# Step 6: Find best portfolio
best = find_optimal_portfolio(results)

best_return, best_volatility, best_sharpe, best_weights = best

print("\nOptimal Portfolio:")
print(f"Return: {best_return:.2f}")
print(f"Volatility: {best_volatility:.2f}")
print(f"Sharpe Ratio: {best_sharpe:.2f}")

print("\nWeights:")
for stock, weight in zip(returns.columns, best_weights):
    print(f"{stock}: {weight:.2%}")