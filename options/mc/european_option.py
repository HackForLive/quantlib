"""
Euler discretization method
"""
import random
import math

import numpy as np


def discrete_random_walk_model(
        underlying_value: float, drift: float, volatility: float, step: float) -> float:
    return drift * underlying_value * step + (
        volatility * underlying_value * math.sqrt(step) * random.random())

"""
|-|-|.|
|-|-|.|
|...|.|
"""

def discrete_mc_single_path(
        spot_value: float, drift: float, volatility: float, step: float, maturity: int) -> float:
    prev = spot_value
    discrete_random_walk_model(
        underlying_value=prev, drift=drift, volatility=volatility, )



def discrete_mc_pricing(
        spot_value: float, drift: float, volatility: float, step: float, 
        n: int, maturity: int) -> float:
    x = np.empty(shape=(n, int(maturity/step)))
    x.fill(spot_value)

    for t in range(0, n):
        for t in range(step, maturity, step):
            val = discrete_random_walk_model(
                underlying_value=underlying_value, drift=drift, volatility=volatility, step=step)

drift * underlying_value * step + (
        volatility * underlying_value * math.sqrt(step) * random.random())

if __name__ == "__main__":
    # current spot value
    S = 100
    # volatility 20%, drift 5%
    vol = 0.2
    drift = 0.05
    # time step
    dt = 0.01
    # interest rate
    r = 0.05
    # number of paths
    n = 1000
    # maturity
    T = 1

