import pandas as pd

df = pd.read_csv("raw_prices_data.csv", index_col=0, parse_dates=True)

print("Before cleaning")
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.index.duplicated().sum())

# Remove duplicates
df = df[~df.index.duplicated(keep="first")]

# Handle missing values (Forward Fill)
df = df.ffill()

# Final safety check
df.dropna(inplace=True)

df.to_csv("cleaned_prices_data.csv")

print("\nAfter cleaning")
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.index.duplicated().sum())

print("cleaned_prices_data.csv created")
