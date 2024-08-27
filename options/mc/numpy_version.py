"""
European call option
"""

import numpy as np

# Parameters
S0 = 100      # initial stock price
K = 105       # strike price
T = 1.0       # time-to-maturity
r = 0.05      # risk-free rate
sigma = 0.2   # volatility
M = 50        # number of time steps
dt = T / M    # length of time interval
I = 250000    # number of paths

# Simulating I paths with M time steps
np.random.seed(0)
S = S0 * np.exp(np.cumsum((r - 0.5 * sigma ** 2) * dt
    + sigma * np.sqrt(dt) * np.random.standard_normal((M + 1, I)), axis=0))
S[0] = S0

# Calculating the Monte Carlo estimator
C0 = np.exp(-r * T) * np.sum(np.maximum(S[-1] - K, 0)) / I

# Results output
print("Value of the European Call Option %5.3f" % C0)
