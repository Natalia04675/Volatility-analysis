from scipy.optimize import brentq

from bs model import bs_call_price


def implied_volatility(
    market_price,
    S,
    K,
    T,
    r
):

    f = (
        lambda sigma:
        bs_call_price(
            S,
            K,
            T,
            r,
            sigma
        ) - market_price
    )

    iv = brentq(
        f,
        0.001,
        3.0
    )

    return iv