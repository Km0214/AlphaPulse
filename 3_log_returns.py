import pandas as pd
import numpy as np

# Load cleaned data
prices = pd.read_csv(
    "cleaned_prices_data.csv",
    index_col=0,
    parse_dates=True
)

# Calculate daily log returns
log_returns = np.log(prices / prices.shift(1)).dropna()

log_returns.to_csv("log_returns.csv")

print(" log_returns.csv created")
