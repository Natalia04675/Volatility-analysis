import yfinance as yf

spy = yf.Ticker("SPY")

dates = spy.options

print(dates)