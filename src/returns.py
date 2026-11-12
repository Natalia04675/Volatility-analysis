import numpy as np


def compute_returns(prices):

    returns = np.log(
        prices / prices.shift(1)
    )

    return returns.dropna()