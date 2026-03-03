import yfinance as yf
import pandas as pd

stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS"]

df_list = []

for stock in stocks:
    temp = yf.download(stock, start="2020-01-01", progress=False)
    temp = temp[["Close"]]
    temp.columns = [stock]
    df_list.append(temp)

# Combine all assets (this creates missing values naturally)
raw_df = pd.concat(df_list, axis=1)

# Introduce duplicates (realistic issue)
raw_df = pd.concat([raw_df, raw_df.iloc[0:5]])

#Introduce missing values intentionally
raw_df.iloc[10:15, 0] = None
raw_df.iloc[20:25, 2] = None

raw_df.to_csv("raw_prices_data.csv")

print(" raw_prices_data.csv created (contains missing values & duplicates)")


# Load cleaned data
prices = pd.read_csv(
    "cleaned_prices.csv",
    index_col=0,
    parse_dates=True
)

# Calculate daily log returns
log_returns = np.log(prices / prices.shift(1)).dropna()

log_returns.to_csv("log_returns.csv")

print("log_returns.csv created")
