import yfinance as yf
import numpy as np

spy = yf.download(
    "SPY",
    start="2020-01-01",
    end="2025-01-01"
)

spy["Log_Return"] = np.log(
    spy["Close"] /
    spy["Close"].shift(1)
)

print(spy["Log_Return"])