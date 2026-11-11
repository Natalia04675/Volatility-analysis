from scipy.stats import norm
import numpy as np

def bs_call_price(
    S,
    K,
    T,
    r,
    sigma
):

    d1 = (
        np.log(S / K)
        + (r + sigma**2 / 2) * T
    ) / (sigma * np.sqrt(T))

    d2 = d1 - sigma * np.sqrt(T)

    call = (
        S * norm.cdf(d1)
        - K * np.exp(-r*T) * norm.cdf(d2)
    )

    return call