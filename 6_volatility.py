import pandas as pd

returns = pd.read_csv(
    "log_returns.csv",
    index_col=0,
    parse_dates=True
)

# Historical volatility (annualized)
historical_vol = returns.std() * (252 ** 0.5)

# Rolling 30-day volatility
rolling_vol = returns.rolling(window=30).std() * (252 ** 0.5)

historical_vol.to_csv("historical_volatility.csv")
rolling_vol.to_csv("rolling_volatility.csv")

print(" Volatility files created")
