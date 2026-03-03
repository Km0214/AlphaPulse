import pandas as pd
import numpy as np

# Load log returns
returns = pd.read_csv(
    "log_returns.csv",
    index_col=0,
    parse_dates=True
)

# Equal-weight portfolio
weights = np.ones(returns.shape[1]) / returns.shape[1]

# Portfolio daily returns
portfolio_returns = returns.dot(weights)

# Parameters
mean = portfolio_returns.mean()
std = portfolio_returns.std()
days = 252
num_simulations = 10000

# Monte Carlo simulation
simulated_returns = np.random.normal(
    mean,
    std,
    size=(days, num_simulations)
)

# Cumulative returns
portfolio_paths = simulated_returns.cumsum(axis=0)

#  FORCE last-day values as 1D ARRAY
final_values = portfolio_paths[-1, :]

print("Shape of final_values:", final_values.shape)  # should be (10000,)

# SAFE DataFrame creation
mc_df = pd.DataFrame(
    final_values,
    index=range(len(final_values)),
    columns=["Final_Return"]
)

mc_df.to_csv("monte_carlo_results.csv", index=False)

print("monte_carlo_results.csv created successfully")
