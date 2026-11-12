from implied_votality import implied_vol
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def build_volatility_smile():

    ticker = yf.Ticker("SPY")

    expiry = ticker.options[0]

    calls = ticker.option_chain(expiry).calls

    spot_price = ticker.history(period="1d")["Close"].iloc[-1]

    risk_free_rate = 0.04

    T = 30 / 365

    strikes = []
    ivs = []

    for _, row in calls.iterrows():

        market_price = row["lastPrice"]
        strike = row["strike"]
        if strike < spot_price * 0.8:
         continue

        if strike > spot_price * 1.2:
         continue

        if market_price <= 0:
            continue

        try:

            iv = implied_vol(
                market_price=market_price,
                S=spot_price,
                K=strike,
                T=T,
                r=risk_free_rate
            )

            strikes.append(strike)
            ivs.append(iv)

        except:
            continue

    df = pd.DataFrame({
        "Strike": strikes,
        "IV": ivs
    })

    return df


def plot_smile(df):

    plt.figure(figsize=(10,6))

    plt.plot(
        df["Strike"],
        df["IV"],
        marker="o"
    )

    plt.title("SPY Volatility Smile")
    plt.xlabel("Strike")
    plt.ylabel("Implied Volatility")

    plt.grid(True)

    plt.show()


if __name__ == "__main__":

    df = build_volatility_smile()

    print(df.head())

    plot_smile(df)