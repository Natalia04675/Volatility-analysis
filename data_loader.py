import yfinance as yf


def load_spy():
    ticker = yf.Ticker("SPY")

    df = ticker.history(
        period="5y",
        interval="1d"
    )

    return df

from data_loader import load_spy

df = load_spy()

print(df.head())