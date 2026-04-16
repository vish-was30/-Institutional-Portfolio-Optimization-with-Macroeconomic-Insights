import pandas as pd

def calculate_returns(data):
    return data.pct_change().dropna()

def calculate_risk_return(returns):
    risk = returns.std()
    mean_return = returns.mean()
    return risk, mean_return

def correlation_matrix(returns):
    return returns.corr()

import numpy as np

def portfolio_performance(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    return portfolio_return, portfolio_volatility

def generate_random_portfolios(num_portfolios, returns):
    results = []
    num_assets = len(returns.columns)

    for _ in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)

        ret, vol = portfolio_performance(weights, returns)
        sharpe = ret / vol

        results.append([ret, vol, sharpe, weights])

    return results

def find_optimal_portfolio(results):
    max_sharpe = max(results, key=lambda x: x[2])
    return max_sharpe