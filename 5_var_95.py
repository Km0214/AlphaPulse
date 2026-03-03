import pandas as pd
import numpy as np

# Load Monte Carlo results
mc = pd.read_csv("monte_carlo_results.csv")

# Calculate VaR at 95% confidence
VaR_95 = np.percentile(mc["Final_Return"], 5)

# # Calculate VaR at 99% confidence
# VaR_95 = np.percentile(mc["Final_Return"], 1)

print(f" Value at Risk (95% confidence): {VaR_95:.4f}")
