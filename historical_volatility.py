import yfinance as yf
import numpy as np

spy = yf.download(
    "SPY",
    start="2020-01-01",
    end="2025-01-01"
)

returns = np.log(
    spy["Close"] /
    spy["Close"].shift(1)
)

returns = returns.dropna()

hv = returns.std() * np.sqrt(252)

print("Historical Volatility:")
print(hv)

import matplotlib.pyplot as plt

rolling_vol = (
    returns
    .rolling(30)
    .std()
    * np.sqrt(252)
)

rolling_vol.plot()

plt.title("30-Day Volatility")
plt.show()