import yfinance as yf

def fetch_stock_data(stocks, start, end):
    data = yf.download(
        stocks,
        start=start,
        end=end,
        group_by='ticker',
        auto_adjust=True,
        threads=False  # 🔥 IMPORTANT FIX
    )
    
    # Extract Adj Close safely
    if isinstance(data.columns, tuple) or hasattr(data.columns, "levels"):
        data = data.xs('Close', axis=1, level=1)
    
    return data.dropna()

from fredapi import Fred
def fetch_interest_rates(api_key):
    fred = Fred(api_key=api_key)
    rates = fred.get_series("FEDFUNDS")
    return rates