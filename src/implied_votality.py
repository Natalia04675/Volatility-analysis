from scipy.optimize import brentq
from black_scholes import call_price

def implied_vol(
    market_price,
    S,
    K,
    T,
    r
):

    f = lambda sigma: (
        call_price(
            S,
            K,
            T,
            r,
            sigma
        )
        - market_price
    )

    return brentq(
        f,
        0.001,
        5
    )


if __name__ == "__main__":

    iv = implied_vol(
        market_price=22.43,
        S=500,
        K=500,
        T=0.25,
        r=0.04
    )

    print(iv)